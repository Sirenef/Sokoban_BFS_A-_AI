import support_function as spf 
import time
from queue import PriorityQueue

'''
//========================//
//          ASTAR         //
//        ALGORITHM       //
//     IMPLEMENTATION     //
//========================//
'''
def AStart_Search(board, list_check_point):
    start_time = time.time()
    ''' A* SEARCH SOLUTION '''
    ''' goal hoặc không có check point '''
    if spf.check_win(board,list_check_point):
        print("Found win")
        return [board]
    ''' khởi tạo start state'''
    start_state = spf.state(board, None, list_check_point)
    list_state = [start_state]
    ''' khởi tạo hàng đợi ưu tiên '''
    heuristic_queue = PriorityQueue()
    heuristic_queue.put(start_state)
    ''' vòng lặp hàng đợi ưu tiên '''
    while not heuristic_queue.empty():
        '''nhận state để tìm kiếm'''
        now_state = heuristic_queue.get()
        ''' nhận vị trí hiện tại người chơi'''
        cur_pos = spf.find_position_player(now_state.board)
        ''' 
        THIS WILL PRINT THE STEP-BY-STEP IMPLEMENTATION OF HOW THE ALGORITHM WORKS, 
        UNCOMMENT TO USE IF NECCESSARY 
        '''
        '''
        time.sleep(1)
        clear = lambda: os.system('cls')
        clear()
        print_matrix(now_state.board)
        print("State visited : {}".format(len(list_state)))
        print("State in queue : {}".format(len(list_visit)))
        '''
        
        ''' nhận list có thể di chuyển '''
        list_can_move = spf.get_next_pos(now_state.board, cur_pos)
        ''' tạo các state từ list có thể di chuyển '''
        for next_pos in list_can_move:
            ''' tạo bảng mới '''
            new_board = spf.move(now_state.board, next_pos, cur_pos, list_check_point)
            ''' nếu bảng này chưa có trong list => bỏ qua state '''
            if spf.is_board_exist(new_board, list_state):
                continue
            ''' nếu 1 hoặc nhiều hộp bị kẹt trong góc => bỏ qua state '''
            if spf.is_board_can_not_win(new_board, list_check_point):
                continue
            ''' tất cả hộp bị ket => bỏ qua state '''
            if spf.is_all_boxes_stuck(new_board, list_check_point):
                continue

            ''' tạo state mới '''
            new_state = spf.state(new_board, now_state, list_check_point)
            ''' kiểm tra state phải goal hay không '''
            if spf.check_win(new_board, list_check_point):
                print("Found win")
                return (new_state.get_line(), len(list_state))
            
            ''' thêm state mới vào hàng ưu tiên và danh sách đã chuyển '''
            list_state.append(new_state)
            heuristic_queue.put(new_state)

            ''' tính time out '''
            end_time = time.time()
            if end_time - start_time > spf.TIME_OUT:
                return []
        end_time = time.time()
        if end_time - start_time > spf.TIME_OUT:
            return []
    ''' không tìm thấy lời giải '''
    print("Not Found")
    return []