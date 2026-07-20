"""
Module: mcu_core.py
Description: Mô phỏng thao tác trên thanh ghi 8-bit và chuyển đổi tín hiệu ADC sang nhiệt độ.
"""

def scale_adc_to_temp(adc_raw: int) -> float:
    """
    Chuyển đổi giá trị ADC 12-bit sang nhiệt độ.

    Args:
        adc_raw (int): Giá trị ADC đầu vào (0 - 4095).

    Returns:
        float: Nhiệt độ đã được chuyển đổi.

    Raises:
        ValueError: Nếu giá trị adc_raw nằm ngoài khoảng 0-4095.
    """
    # Kiểm tra giới hạn của ADC 12-bit
    if not (0 <= adc_raw <= 4095):
        raise ValueError("Giá trị ADC đầu vào phải nằm trong khoảng từ 0 đến 4095.")

    # Tính toán điện áp và nhiệt độ theo công thức
    v_in = (adc_raw / 4095.0) * 3.3
    temperature = (v_in - 0.1) * 50.0
    
    return temperature


def modify_register(reg_val: int, bit_pos: int, action: str) -> int:
    """
    Mô phỏng thao tác trên thanh ghi 8-bit bằng toán tử Bitwise.

    Args:
        reg_val (int): Giá trị hiện tại của thanh ghi.
        bit_pos (int): Vị trí bit cần thao tác (0 - 7).
        action (str): Hành động cần thực hiện ('SET', 'CLEAR', 'TOGGLE', 'READ').

    Returns:
        int: Giá trị thanh ghi sau khi thao tác (với SET, CLEAR, TOGGLE) 
             hoặc trạng thái của bit (với READ).

    Raises:
        IndexError: Nếu vị trí bit không hợp lệ (nằm ngoài khoảng 0-7).
        ValueError: Nếu chuỗi action không hợp lệ.
    """
    # Kiểm tra tính hợp lệ của vị trí bit trên thanh ghi 8-bit
    if not (0 <= bit_pos <= 7):
        raise IndexError("Vị trí bit phải nằm trong khoảng từ 0 đến 7.")

    action = action.upper()
    
    # Thực hiện các toán tử Bitwise
    if action == "SET":
        return reg_val | (1 << bit_pos)
    elif action == "CLEAR":
        return reg_val & ~(1 << bit_pos)
    elif action == "TOGGLE":
        return reg_val ^ (1 << bit_pos)
    elif action == "READ":
        return (reg_val >> bit_pos) & 1
    else:
        raise ValueError("Action không hợp lệ. Chỉ hỗ trợ: SET, CLEAR, TOGGLE, READ.")

# Gọi hàm thử nghiệm để kiểm tra
if __name__ == "__main__":
    ket_qua = modify_register(0, 3, "SET")
    print("Giá trị thanh ghi sau khi SET:", ket_qua)