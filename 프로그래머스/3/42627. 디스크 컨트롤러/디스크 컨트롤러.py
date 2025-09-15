import heapq

def solution(jobs):

    num_jobs = len(jobs)
    
    # 1. 요청 시각(s) 기준으로 모든 작업을 오름차순 정렬합니다.
    jobs.sort(key=lambda x: x[0])
    
    waiting_queue = []  # 대기 큐로 사용할 최소 힙
    total_turnaround_time = 0
    current_time = 0
    jobs_processed = 0
    job_idx = 0
    
    # 2. 모든 작업이 처리될 때까지 시뮬레이션 루프를 실행합니다.
    while jobs_processed < num_jobs:
        
        # 3. 현재 시간(current_time)까지 요청된 모든 작업을 대기 큐(힙)에 추가합니다.
        while job_idx < num_jobs and jobs[job_idx][0] <= current_time:
            request_time, duration = jobs[job_idx]
            # 우선순위: (소요 시간, 요청 시각) 순서로 힙에 push
            heapq.heappush(waiting_queue, (duration, request_time))
            job_idx += 1
            
        # 4. 대기 큐에 처리할 작업이 있는 경우
        if waiting_queue:
            # 우선순위가 가장 높은 작업을 꺼냅니다.
            duration, request_time = heapq.heappop(waiting_queue)
            
            # 작업을 실행하고 현재 시간을 업데이트합니다.
            current_time += duration
            
            # 반환 시간(종료 시간 - 요청 시간)을 계산하여 누적합니다.
            turnaround_time = current_time - request_time
            total_turnaround_time += turnaround_time
            
            jobs_processed += 1
        # 5. 대기 큐가 비어있는 경우 (디스크가 유휴 상태)
        else:
            # 아직 들어올 작업이 남아있다면, 다음 작업의 요청 시점으로 시간을 점프시킵니다.
            if job_idx < num_jobs:
                current_time = jobs[job_idx][0]
    
    # 6. 평균 반환 시간을 계산하고 정수 부분만 반환합니다.
    return total_turnaround_time // num_jobs