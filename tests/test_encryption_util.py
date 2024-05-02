from mercury.utils.EncryptionUtil import encrypt_by_md5


def test_encrypt_by_md5():
    """"""
    data = encrypt_by_md5("test-user+", "key")
    assert data == "2b9119ecd2676e197d714d8510b02e7d"
