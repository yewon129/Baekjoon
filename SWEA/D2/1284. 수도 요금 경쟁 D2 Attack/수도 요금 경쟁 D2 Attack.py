T = int(input())
for tc in range(1, T+1):
    # A: 1리터당 P원 / B : 기본요금 Q, 월간 사용량 R리터 이상이면 1리터당 +S원 / 물 사용량 W
    P, Q, R, S, W = map(int, input().split())

    A = P * W
    B = Q
    if W > R:
        B += (W-R) * S

    if A > B:
        print(f'#{tc} {B}')
    else:
        print(f'#{tc} {A}')