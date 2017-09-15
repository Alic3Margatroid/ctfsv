Chúng ta truy cập trang http://oreo3306.scoreboard.ns01.info/login.php có giao diện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Oreo/login.PNG)

Vào trang đăng ký, view source sẽ thấy trang get_invite_code.php. Vào trang này, trong source code kéo xuống dưới cùng sẽ thấy mã đăng ký: TINHYEUKHONGCOLOI. Dùng mã này để đăng ký và đăng nhập vào giao diện chính của trang.

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Oreo/home.png)

Vào view source để xem code sẽ thấy các function về authentication:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Oreo/viewsource.png)

Trang web quản lý quyền của user qua cookie gồm 2 phần là session và hash. Mục tiêu của chúng ta là craft cookie của admin.

Session của chúng ta có dạng : base64((1 chuỗi json encode trong đó có trường username do ta kiểm soát) xor key)
Có thể thấy nếu chúng ta đem xor đoạn (username xor key) với username thì sẽ có lại key (bị rotate).

Ý tưởng chúng ta ở đây là sẽ dùng 1 username có độ dài lớn hơn độ dài tiềm năng của key, và các chữ cái trong username là giống nhau (ví dụ như 50 chữ a). Sau đó đem xor toàn bộ session với 1 chuỗi toàn a, pattern liền nhau nào lặp lại (hoặc lặp lại 1 phần) sẽ là key bị rotate.

Với tên đăng nhập là 50 chữ a, ta có session: HEQdUDsHMiRREQhkfmAKGXZ8Jm12cSdkYCJnfmkkei4mMydsFycICGBmEGoRVDEzR1oGTlQQUghJBkhJRwxVBwYHC0I/BSEgRFJTJ1JAIzdUVQZCUFMJS0kGSElHDFUHBgcLQj8FISBEUhBqEVInNUdREwELED5jcCJhbXI1dSggLit6ECMVDmxncw52dRsTYBYa

Base64 decode và xor với a, ta sẽ nhìn thấy đoạn lặp lại ở đây là (g)(&m4fgfj#^d@A%32F3!BV54g#12h*

Sau đó ta rotate đoạn này và lần lượt đem xor với session cho tới khi ra được 1 đoạn có chứa "username", ta nhận được:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Oreo/key.PNG)

Key sẽ là gfj#^d@A%32F3!BV54g#12h*(g)(&m4f, và các trường cần thiết để ta tạo cookie và hash như trên hình.

Dựa vào source code, ta sẽ craft được cookie của admin:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Oreo/craft.PNG)

và có flag:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Oreo/flag.PNG)

flag: Flag{are_you_still_xorring_me?}