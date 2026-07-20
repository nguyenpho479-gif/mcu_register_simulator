# 1. Prompt
**Role:** You are a Senior Embedded Software Engineer.
**Context:** The software will be used in an undergraduate laboratory for Robot and AI students.
**Task:** Develop a Python module named `mcu_core.py` with `scale_adc_to_temp` and `modify_register` functions.

# 2. AI Response
AI đã sinh ra mã nguồn cơ bản, áp dụng đúng công thức V_in = (adc_raw / 4095) * 3.3 và các toán tử bitwise.

# 3. Evaluation
- Thuật toán: Chính xác.
- Type Hint: Đầy đủ.
- Xử lý ngoại lệ: Chưa phân biệt rõ ValueError và IndexError.
- Docstring: Cần Việt hóa để dễ hiểu hơn.

# 4. Revision
- Cập nhật và Việt hóa Docstring.
- Bổ sung kiểm tra IndexError chặt chẽ.
- Định dạng lại code đúng chuẩn PEP8.