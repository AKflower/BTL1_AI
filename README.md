# BTL1_AI: N-Queens Problem
## Mục tiêu
Hiện thực các giải thuật Tìm kiếm cơ bản 
Giải được bài toán N-queens
## Giới thiệu
Bài toán N-queens là bài toán yêu cầu đặt N quân hậu lên bàn cờ NxN sao cho không có bất kì cặp quân 
hậu nào uy hiếp nhau (hậu uy hiếp theo luật cờ vua)

## Định dạng không gian trạng thái

Để biểu diễn một cách trực quan và ngắn gọn, ta dùng mảng x để biểu diễn bàn cờ NxN, trong đó thứ tự của phần tử tương ứng vị trí cột, mỗi phần tử của x là vị trí hàng của quân hậu.

* State: Mảng x gồm n phần tử. 
       x[i] = j ∀ 1 ≤ i ≤ n, 1 ≤ j ≤ n
* Initial state: x[i] = 0 ∀ 1 ≤ i ≤ n
* Goal state: ∀ 1 ≤ i ≤ n, 1 ≤ k ≤ n, i ≠ k => x[i] ≠ x[k], |i-k| ≠ |x[i]-x[k]|
* Legal moves: <br>
  Hàm **checkRow** kiểm tra hàng ngang.
  <pre>
  checkRow(i,j,x):
    for (k=1,k<=n,k++):
      if (i ≠ k) and (j == x[k]): return False
    return True
  </pre>
  Hàm **checkDiangonal** kiểm tra đường chéo.
  <pre>
  checkDiagonal(i,j,x):
    for (k=1,k<=n,k++):
      if (i ≠ k) and (abs(i-k) == abs(j-x[k])): return False
    return True
  </pre>
