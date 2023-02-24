def solution(b, w, tws):
    answer = 0
    bridge = [0] * b
    bsum = sum(bridge)
    while bridge:
        bsum -= bridge.pop(0)
        answer += 1
        
        if tws:
            if bsum + tws[0] <= w:
                truck = tws.pop(0)
                bsum += truck
                bridge.append(truck)
            else:
                bridge.append(0)
        else:
            answer += len(bridge)
            bridge = []
            
    return answer