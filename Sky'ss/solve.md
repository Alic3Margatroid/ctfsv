Truy cập vào trang http://mtp.scoreboard.ns01.info/ chúng ta thấy giao diện như sau:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Sky'ss/home.PNG)

Chuyển qua lại giữa các trang menu chúng ta thấy trường ?page= là nơi có khả năng có lỗi đầu tiên. Với việc url có dạng ?page=fanboard, etc... thì sau khi nhận trường page trang web sẽ thêm đuôi (.php) vào sau.

Thử LFI với base64-encode thấy xuất hiện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Sky'ss/convertb64.PNG)

=> LFI có vẻ đúng hướng.

Khả năng ở đây trang web đã filter 1 trường nào đó trong payload ta submit. Thử với payload ?page=base64 xác nhận điều này:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Sky'ss/b64.PNG)

Vậy chúng ta thay vì sử dụng base64 convert thì sẽ sử dụng 1 hàm khác có tác dụng tương tự, ở đây chúng ta sẽ sử dụng convert.quoted-printable-encode. Đọc page fanboard với payload này chúng ta sẽ có flag:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/Sky'ss/flag.PNG)

flag: Flag{4m^_Th4m`___b3N^__3m}