Truy cập vào trang web http://dotard.scoreboard.ns01.info/ chúng ta sẽ thấy 1 giao diện login: 

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Dotard2/login.PNG)

Đọc source sẽ thấy dòng comment "miracle/champion" là username và password sử dụng để đăng nhập.

Sau đăng nhập:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Dotard2/home.PNG)

Click vào 1 link sẽ thấy url có dạng detail.php?id=1. Thử payload là ?id=1' cho trang error: 

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Dotard2/error.PNG)

Có thể thấy id bị lỗi sqli và ở đây server sử dụng sqlite. Sqlite có 1 table khá thú vị là sqlite_master trong đó lưu lại các câu query được sử dụng trong cột sql. Chúng ta sẽ sử dụng union injection (1 chút test sẽ thấy số cột cần thiết cho union ở đây là 3) với payload  union select 1,1,sql from sqlite_master limit x,1 -- - (x tăng dần) để đọc từng câu query một. Với x=2 ta có:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Dotard2/flagquery.PNG)

Vậy bảng cần đọc là "hithere" và chỉ có 1 cột duy nhất là "flag". Đọc bảng này chúng ta có flag:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Dotard2/flag.PNG)

flag: FLAG{b4s1c__Un10n_sk1lL}
