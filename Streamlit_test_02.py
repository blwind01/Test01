import streamlit as st
import numpy as np
from PIL import Image

# 초기 gen_img 생성 (0과 1 사이의 값)
gen_img = np.random.rand(512, 128, 3)

# Streamlit UI 설정
st.title("Number Input with Image Display")

# 슬라이더 값 입력
st.sidebar.header("Adjust the Sliders (0 to 1)")
values = [
    st.sidebar.slider(f"Number {i+1}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    for i in range(5)
]

# gen_img 배열을 업데이트하는 함수
def update_gen_img(gen_img, values):
    # 슬라이더 값에 따라 gen_img 채널을 조정
    gen_img[:, :, 0] = values[0]  # R 채널
    gen_img[:, :, 1] = values[1]  # G 채널
    gen_img[:, :, 2] = values[2]  # B 채널
    return (gen_img * 255).astype(np.uint8)  # 0-255 범위로 변환

# 입력 이미지 업데이트
gen_img_scaled = update_gen_img(gen_img, values)
input_image = Image.fromarray(gen_img_scaled)

# 출력 이미지 생성 (예시로 Number 4와 Number 5 슬라이더 값 사용)
output_color = (int(values[3] * 255), int(values[4] * 255), 0)
output_image = Image.new("RGB", (128, 512), output_color)

image_width = 120

# 좌우로 이미지 배치
col1, col2 = st.columns(2)

with col1:
    st.write("### Input Image")
    st.image(input_image, caption="Input", width=image_width)

with col2:
    st.write("### Output Image")
    st.image(output_image, caption="Output", width=image_width)
