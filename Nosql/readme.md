Chúng ta truy cập trang http://nosqlinjection.scoreboard.ns01.info/auth.php và có giao diện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Nosql/auth.PNG)

Giao diện gồm đăng nhập và đăng ký. Mục tiêu của bài là đăng nhập dưới tên admin.

Đọc source code ta thấy có đoạn:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Nosql/source.PNG)

Cơ chế lưu user ở đây là lưu theo directory. Mỗi user đăng ký mới sẽ được cấp 1 directory theo username. Username được filter "../" thành "" hoặc "..\\" thành "". Việc check trùng tài khoản được thực hiện đơn giản là so username nhận được với tất cả directory trong thư mục users. 

Chúng ta muốn đăng nhập bằng tài khoản admin, vậy ở đây chúng ta sẽ tạo 1 tài khoản admin riêng của chúng ta, ghi đè lên tài khoản cũ. Thay vì "../" chúng ta sẽ dùng "....//", từ đó bypass được filter.

Vậy đăng ký tài khoản mới của chúng ta sẽ là "....//users/admin", password tùy chọn:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Nosql/register.PNG)

Đăng nhập lại bằng admin, chúng ta có flag:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Nosql/flag.PNG)

flag: Flag{you_cant_have_sql_injection_if_you_dont_use_sql}