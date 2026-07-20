import pytest
from mcu_core import scale_adc_to_temp, modify_register

def test_scale_adc_to_temp():
    # Kiểm tra giá trị hợp lệ
    assert scale_adc_to_temp(2048) == pytest.approx(77.52, rel=1e-1)
    # Kiểm tra lỗi khi giá trị nằm ngoài phạm vi
    with pytest.raises(ValueError):
        scale_adc_to_temp(5000)

def test_modify_register():
    # Kiểm tra thao tác SET
    assert modify_register(0, 3, "SET") == 8
    # Kiểm tra thao tác CLEAR
    assert modify_register(8, 3, "CLEAR") == 0
    # Kiểm tra lỗi khi vị trí bit không hợp lệ
    with pytest.raises(IndexError):
        modify_register(0, 10, "SET")