
fn extract_byte(val: u32, position: u8) -> u8 {
    return val << (position * 8) & 0xff;
}