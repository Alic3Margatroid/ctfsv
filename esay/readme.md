Chúng ta truy cập vào trang http://hteasy.scoreboard.ns01.info/ và có giao diện:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/esay/home.PNG)

Truy cập 1 vài link, chúng ta thấy server sử dụng include với ?page=, dẫn tới ý tưởng LFI.

Test 1 lúc để thử đọc file /etc/passwd, chúng ta sẽ thấy có filter theo kiểu đổi "../" thành "", và sẽ bypass bằng cách sử dụng "....//".

Tới đây chúng ta có thể đọc /etc/passwd:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/esay/passwd.PNG)

Thử dùng LFI để đọc các file khác, ta thấy có 1 file khá thú vị là apache log:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/esay/apachelog.PNG)

Mò mẫm một hồi mới ngộ ra rằng ip ở đây là địa chỉ public thật của chúng ta. Ở đây ip của chúng ta là 27.72.58.160. Truy cập ../logs/27.72.58.160.log:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/esay/log.PNG)

Có vẻ như file log này giống như log apache thường, chỉ log lại method, uri và http version, sau đó server đọc file log và hiển thị trực tiếp, dẫn tới ý tưởng inject code php. Ta sẽ thử truyền thêm 1 parameter mới là code mà ta định thực thi. Tuy nhiên khi truyền qua url browser thì một số ký tự sẽ bị urlencode, dẫn tới không chạy được code:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/esay/fail.PNG)

Vậy chúng ta sẽ truyền qua burp để tránh bị encode. Tuy nhiên trong burp thì việc url truyền nguyên space là không thể thực hiện. Vậy chúng ta sẽ tìm cách không truyền space nữa. Và php có 1 lựa chọn rất tuyệt vời là &lt;?="string"?&gt; tương đương với &lt;?php echo "string"?&gt;, vậy nên ta sẽ dùng payload là &lt;?=system('ls')&gt;:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/esay/ls.PNG)

và đọc file fgdklnatgrtiuwtgwnsdfgnbldgrhsdgragafdfa_flag.txt:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/esay/flag.PNG)

flag: Flag{0a7edb17adcdbf30da763fca0b4919523927f59e}