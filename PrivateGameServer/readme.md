Truy cập vào trang http://viettel.scoreboard.ns01.info/index.php chúng ta sẽ thấy 1 giao diện login:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/PrivateGameServer/Login.PNG)

Vào source, download file zip về xem chúng ta sẽ thấy 2 file là index.php và forgot.php. Index.php:

<?php 
    include 'config.php';
    session_start();
    if(isset($_POST['username']) && isset($_POST['password'])){
        if($_POST['username']==="butbibutmay" && $_POST['password']===$admin_pw){
            die('Here is your flag: '.$Flag);
        } else {
            die('Incorrect username/password');
        }
    }

?>

chỉ chúng ta rằng nhiệm vụ là cần đăng nhập user "butbibutmay" để có flag. Forgot.php có đoạn sau:

function make_token(){
        global $key;
        $salt = "^*@&24";
        srand((int)($salt.$key));
		$token = "";
        for($i = 0; $i < 32; $i++) {
            $randomDigit = (string)rand() % 10;
            $token .= "," . $randomDigit;
        }
        $token = str_replace(",", "", $token);
        return $token;
    }

    if(isset($_POST['username'])){
        $usn = (string)$_POST['username'];
        if($usn === 'butbibutmay'){
            $token = make_token();
            savedb(session_id(),$token);
            die("Token sent to butbibutmay's email. Please visit link 'forgot.php?verify_token=[The token you received]' to get password!");
        } else {
            die('Invalid username');
        }
    }

    if(isset($_GET['verify_token'])){
        $t = (string)$_GET['verify_token'];
        verify_token(session_id(),$t);
    }

Chúng ta cần phải cung cấp 1 token được sinh ra bởi hàm make_token cho forgot.php, nếu đúng sẽ có password và từ đó có flag. Hàm make token ở đây lấy 1 salt là "^*@&24", sau đó nối với $key trong file config.php để làm seed random. Token sẽ là 1 chuỗi int có giá trị các chữ số từ 0 -> 9 được tính qua hàm random()%10. Điều đặc biệt ở đây là seed được tạo thông qua việc nối salt vs key, sau đó chuyển về kiểu int, trong khi đó salt bắt đầu bởi 1 ký tự khác số, dẫn tới seed ở đây sẽ là 0. Việc hàm random có 1 seed cố định như vậy dẫn tới việc nếu chúng ta sử dụng 1 phiên bản php tương đối giống với phiên bản php của server, và thực hiện hàm make_token() với seed = 0 thì chúng ta sẽ có token chính xác.

Dựa vào phiên bản apache và ubuntu server, chúng ta có thể đoán ở đây sử dụng php 7.0. Chúng ta thực hiện chạy make_token() với php 7.0 sẽ được token = 36753562912709360626187920237592. Nhập vào và chúng ta có password:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/PrivateGameServer/password.PNG)

và đăng nhập vs password này và username butbibutmay chúng ta có flag:

![alt text](https://raw.githubusercontent.com/Alic3Margatroid/ctfsv/master/PrivateGameServer/flag.PNG)

flag: Flag{U__g0t_th1s_S3rv3r}