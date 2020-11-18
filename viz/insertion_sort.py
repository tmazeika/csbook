from manim import *
import copy

ARR_LEN = 7

def sorted_squares(arr):
    return sorted(arr, key=lambda s: s.submobjects[0].get_value())

class InsertionSort(Scene):
    def construct(self):
        in_squares = [Square().set_stroke(BLACK, width=5, opacity=1)
                      for _ in range(ARR_LEN)]
        out_squares = copy.deepcopy(in_squares)

        in_nums = [Integer(n).set_fill(BLACK, opacity=1).set_width(0.6)
                   for n in [2, 7, 6, 9, 1, 0, 3]]
        for i, n in enumerate(in_nums):
            in_squares[i].add(n)
        
        in_arr = Group(*in_squares).arrange().shift(UP * 2)
        for s in in_squares:
            s.save_state()
        tmp_arr = []
        out_arr = Group(*out_squares).arrange().shift(DOWN * 2)

        last_head = None
        def next_iter(head):
            nonlocal last_head
            anims = []
            if last_head:
                anims.append(ApplyMethod(last_head.set_stroke, BLACK))
            anims.append(ApplyMethod(head.set_stroke, TEAL))
            last_head = head
            self.play(*anims)
            tmp_arr.append(head.copy())
            new_arr = sorted_squares(tmp_arr)
            self.play(*[ApplyMethod(s.move_to, out_arr[i].get_center())
                        for i, s in enumerate(new_arr)])

        self.add(in_arr)
        for s in in_squares:
            next_iter(s)
        self.play(ApplyMethod(last_head.set_stroke, BLACK))
        self.wait(3)
        self.play(*[FadeOut(s) for s in tmp_arr])