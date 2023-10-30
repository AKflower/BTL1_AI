# BTL1_AI: N-Queens Problem
## Mục tiêu
Hiện thực các giải thuật Tìm kiếm cơ bản 
Giải được bài toán N-queens
## Giới thiệu
Bài toán N-queens là bài toán yêu cầu đặt N quân hậu lên bàn cờ NxN sao cho không có bất kì cặp quân 
hậu nào uy hiếp nhau (hậu uy hiếp theo luật cờ vua)

## Định dạng không gian trạng thái

Để biểu diễn một cách trực quan và ngắn gọn, ta dùng mảng x để biểu diễn bàn cờ NxN, trong đó thứ tự của phần tử tương ứng vị trí cột, mỗi phần tử của x là vị trí hàng của quân hậu.

* **State:** Mảng x gồm n phần tử. 
       x[i] = j ∀ 0 ≤ i ≤ n-1, 0 ≤ j ≤ n-1
* **Initial state:** x[i] = -1 ∀ 0 ≤ i ≤ n-1
* **Goal state:** ∀ 0 ≤ i ≤ n-1, 0 ≤ k ≤ n-1, i ≠ k => x[i] ≠ x[k], |i-k| ≠ |x[i]-x[k]|
* **Legal moves:** <br>
  Hàm **checkRow** kiểm tra hàng ngang.
  <pre>
  function checkRow(i, j, x):
    n=len(x)
    for k from 0 to n do:
        if i ≠ k and j = x[k] then
            return False
    end for
    return True
  end function
  </pre>
  Hàm **checkDiangonal** kiểm tra đường chéo.
  <pre>
  function checkDiagonal(i, j, x):
    n=len(x)
    for k from 0 to n-1 do:
        if i ≠ k and abs(i - k) = abs(j - x[k]) then
            return False
        end if
    end for
    return True
   end function
  </pre>
  Với điều kiện 0 ≤ i ≤ n-1, 0 ≤ j ≤ n-1, 0 ≤ k ≤ n-1, ta có:
    + **(1)** <pre>x[i] = -1 --> x[i] = j, if (checkRow(i,j,x)) and (checkDiangonal(i,j,x))</pre>
    + **(2)** <pre>x[i] = k --> x[i] = j, if (checkRow(i,j,x)) and (checkDiangonal(i,j,x))</pre>
