import streamlit as st
import time

st.set_page_config(page_title="Mô phỏng câu lệnh IF", layout="wide")

st.title("MÔ PHỎNG CÂU LỆNH IF TRONG PYTHON")
st.subheader("Bài toán: Kiểm tra số chẵn – lẻ")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔢 Nhập dữ liệu")
    n = st.number_input("Nhập số nguyên n", value=5)

    st.markdown("### 🧾 Code Python")
    st.code(
        """n = int(input())
if n % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")""",
        language="python"
    )

    run = st.button("▶ Chạy mô phỏng")

with col2:
    st.markdown("### 🧠 Quá trình mô phỏng")

    if run:
        st.write(f"Giá trị n = {n}")
        time.sleep(0.8)

        st.write("Kiểm tra điều kiện: n % 2 == 0 ?")
        time.sleep(1)

        if n % 2 == 0:
            st.success("Điều kiện ĐÚNG → Thực hiện nhánh IF")
            time.sleep(0.8)
            st.info("Kết luận: n là số CHẴN")
        else:
            st.warning("Điều kiện SAI → Thực hiện nhánh ELSE")
            time.sleep(0.8)
            st.info("Kết luận: n là số LẺ")
