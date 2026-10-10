# Lab 1 Answers — Sultan Syarief Usman (5024231006)

## Q1: What is the output of `ros2 node list` when turtlesim is running?
```
/turtlesim
```
Ketika `turtlesim_node` dijalankan, hanya ada satu node aktif yaitu `/turtlesim`.

## Q2: What topics does the turtlesim node subscribe to and publish?
**Publishes (output):**
- `/turtle1/color_sensor` — sensor warna di bawah kura-kura
- `/turtle1/pose` — posisi dan orientasi kura-kura (x, y, theta, linear_velocity, angular_velocity)

**Subscribes (input):**
- `/turtle1/cmd_vel` — menerima perintah gerak berupa `geometry_msgs/msg/Twist`

## Q3: What is the difference between a topic and a service in ROS 2?
- **Topic**: Komunikasi **publish-subscribe** yang bersifat *asynchronous* dan *many-to-many*. Publisher mengirim pesan secara terus-menerus tanpa perlu menunggu respons. Cocok untuk data stream seperti sensor.
- **Service**: Komunikasi **request-response** yang bersifat *synchronous* dan *one-to-one*. Client mengirim request dan menunggu server memberikan response. Cocok untuk perintah yang perlu konfirmasi, misalnya spawn turtle baru.

## Q4: What message type does `/turtle1/cmd_vel` use?
```
geometry_msgs/msg/Twist
```
Tipe ini terdiri dari dua komponen `Vector3`:
- `linear` (x, y, z) — kecepatan translasi
- `angular` (x, y, z) — kecepatan rotasi

Untuk turtlesim (2D), yang digunakan hanya `linear.x` (maju/mundur) dan `angular.z` (putar kiri/kanan).

## Q5: What happens when you change `ROS_DOMAIN_ID`?
`ROS_DOMAIN_ID` berfungsi sebagai **isolasi jaringan** di ROS 2. Node yang memiliki `ROS_DOMAIN_ID` berbeda **tidak bisa saling berkomunikasi** meskipun berada di jaringan yang sama. Ini penting di lingkungan lab agar sistem robot mahasiswa satu tidak mengganggu mahasiswa lain. Nilai yang valid adalah 0–101.

## Q6: How does `ros2 param set` change behavior without restarting the node?
ROS 2 menyediakan **Parameter Server** di setiap node. Ketika parameter diubah menggunakan `ros2 param set`, node menerima notifikasi perubahan melalui callback (`add_on_set_parameters_callback`). Karena node membaca nilai parameter di setiap iterasi timer (`get_parameter()`), perubahan langsung tercermin pada perilaku node tanpa perlu restart.

Contoh:
```bash
ros2 param set /circle_driver angular_speed 2.5
```
Kura-kura langsung berubah radius lingkarannya karena `angular_speed` yang baru digunakan di setiap publish berikutnya.

## Q7: What does `colcon build --symlink-install` do?
`colcon build` adalah build tool untuk ROS 2 workspace. Flag `--symlink-install` membuat **symbolic link** dari source code ke folder install, sehingga ketika kita mengubah file Python, perubahan langsung berlaku **tanpa perlu build ulang**. Ini sangat berguna saat development karena mempercepat iterasi.
