from manim import *
import copy

config['pixel_height'] = 500

ARR_LEN = 7

def sort_squares(arr):
    return arr.sort(key=lambda s: s.submobjects[0].get_value())

class InsertionSort(Scene):
    def construct(self):
        squares = [Square().set_stroke(BLACK, width=5, opacity=1)
                   for _ in range(ARR_LEN)]

        nums = [Integer(n).set_fill(BLACK, opacity=1).set_width(0.6)
                for n in [2, 7, 6, 9, 1, 0, 3]]
        for i, n in enumerate(nums):
            squares[i].add(n)

        arr = Group(*squares).arrange().shift(0.5 * DOWN)
        ref_arr = copy.deepcopy(arr)
        
        left = [squares[0]]
        right = squares[1:]

        def gen_brace(on_left):
            nonlocal left, right
            if on_left:
                b = Brace(Group(*left)).set_fill(BLUE)
                return (b, b.get_text('Sorted')
                    .scale(1.5)
                    .set_color(BLUE)
                    .set_background_stroke(color=BLUE))
            else:
                b = Brace(Group(*right)).set_fill(GRAY)
                return (b, b.get_text('Unsorted')
                    .scale(1.5)
                    .set_color(GRAY)
                    .set_background_stroke(color=GRAY))

        bl, blt = gen_brace(True)
        br, brt = gen_brace(False)

        def next_pass():
            nonlocal ref_arr, left, right, bl, blt, br, brt
            head = right[0]
            self.play(ApplyMethod(head.set_stroke, BLUE))
            self.play(ApplyMethod(head.shift, 2 * UP))
            left.append(head)
            right = right[1:]
            sort_squares(left)
            new_bl, new_blt = gen_brace(True)
            new_br, new_brt = gen_brace(False)

            def move(i):
                def f(s):
                    return s.move_to(ref_arr[i].get_center()).set_stroke(BLACK)
                return f

            anims = [ApplyFunction(move(i), s) for i, s in enumerate(left)]
            if right:
                anims += [ReplacementTransform(l, r) for l, r
                          in [(bl, new_bl), (blt, new_blt), (br, new_br), (brt, new_brt)]]
            else:
                anims += [ReplacementTransform(l, r) for l, r
                          in [(bl, new_bl), (blt, new_blt)]]
                anims += [FadeOut(br), FadeOut(brt)]
            self.play(*anims)
            bl, blt, br, brt = new_bl, new_blt, new_br, new_brt

        self.play(*[FadeIn(o) for o in [arr, bl, blt, br, brt]])
        for _ in range(len(right)):
            next_pass()
        self.wait(3)
        self.play(*[FadeOut(o) for o in [arr, bl, blt]])
