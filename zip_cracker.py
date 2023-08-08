import zipfile
import itertools
import time


def main():
    zip_file_path = 'target/target1-1.zip'  # ファイル名
    password_length = 4  # パスワードの長さ
    charset = "0123456789"  # パスワードに使う文字

    crack_zip_password(zip_file_path, password_length, charset)


def crack_zip_password(zip_file_path, password_length, charset):
    """
    パスワード付きZIPファイルを総当りで解く関数
    :param zip_file_path: パスワード付きZIPファイルのパス
    :param password_length: パスワードの長さ
    :param charset: パスワードに使用する文字セット
    """
    zip_file = zipfile.ZipFile(zip_file_path)

    start_time = time.time()
    count = 1

    for password in itertools.product(charset, repeat=password_length):
        password = ''.join(password)
        print(f"{count}回目 次のパスワードを試します：{password}")
        try:
            zip_file.extractall(pwd=password.encode())
            print(f"パスワードが見つかりました: {password}")
            end_time = time.time()
            print(f"パスワード見つけるのに{(end_time - start_time):.3f}秒かかりました")
            return
        except Exception as e:
            count += 1
            continue

    print("パスワードが見つかりませんでした。")


if __name__ == "__main__":
    main()
