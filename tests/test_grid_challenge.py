# test_grid_challenge.py
import unittest
from io import StringIO
from unittest.mock import patch
from Algorithms.Grid import Grid_challenge as Grid

# คลาสสำหรับการทดสอบ
class TestGridChallenge(unittest.TestCase):
    
    def test_single_row_grid(self):
        """ทดสอบด้วย grid ที่มีแถวเดียว"""
        grid = ["abc"]
        self.assertEqual(Grid(grid), "YES")
        
        grid = ["cba"]
        self.assertEqual(Grid(grid), "YES")  # เรียงลำดับได้เป็น "abc"
    
    def test_single_column_grid(self):
        """ทดสอบด้วย grid ที่มีคอลัมน์เดียว"""
        grid = ["a", "b", "c"]
        self.assertEqual(Grid(grid), "YES")

    
    def test_small_grid_valid(self):
        """ทดสอบด้วย grid ขนาดเล็กที่เรียงลำดับได้"""
        grid = ["abc", "def", "ghi"]
        self.assertEqual(Grid(grid), "YES")
        
        grid = ["cba", "fed", "ihg"]
        self.assertEqual(Grid(grid), "YES")  # หลังเรียงแถวแล้ว คอลัมน์เรียงลำดับ
    
    def test_small_grid_invalid(self):
        """ทดสอบด้วย grid ขนาดเล็กที่เรียงลำดับไม่ได้"""
        grid = ["abc", "hgf", "def"]
        self.assertEqual(Grid(grid), "NO")  # คอลัมน์ไม่เรียงลำดับหลังจากเรียงแถว
    
    def test_grid_with_mixed_cases(self):
        """ทดสอบด้วย grid ที่มีทั้งตัวพิมพ์เล็กและตัวพิมพ์ใหญ่"""
        grid = ["aB", "bA"]
        # หลังจากเรียงแถว: ["Ba", "Ab"]
        # คอลัมน์: ["BA", "ab"] - ต้องเป็น NO เพราะ B > A
        self.assertEqual(Grid(grid), "NO")
    
    def test_grid_with_repeated_characters(self):
        """ทดสอบด้วย grid ที่มีตัวอักษรซ้ำ"""
        grid = ["aaa", "bbb", "ccc"]
        self.assertEqual(Grid(grid), "YES")
        
        grid = ["aaa", "aaa", "bbb"]
        self.assertEqual(Grid(grid), "YES")
    
    def test_grid_edge_cases(self):
        """ทดสอบกรณีพิเศษ"""
        # กรณี grid ว่าง
        self.assertEqual(Grid([]), "YES")  # หรืออาจจะเป็น edge case ที่ต้องจัดการเฉพาะ
        
        # กรณี grid มีแถวว่าง
        grid = ["", ""]
        self.assertEqual(Grid(grid), "YES")
    
    def test_grid_with_borderline_sorted(self):
        """ทดสอบกรณีที่การเรียงลำดับแบบพอดี"""
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        # หลังเรียงแถว: ["abcde", "fghij", "klmno", "pqrst", "uvwxy"]
        # คอลัมน์เรียงลำดับพอดี
        self.assertEqual(Grid(grid), "YES")
    
    def test_grid_with_almost_sorted(self):
        """ทดสอบกรณีที่เกือบเรียงลำดับ"""
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywvu"]
        self.assertEqual(Grid(grid), "YES")
    
    def test_example_from_problem(self):
        """ทดสอบตัวอย่างจากโจทย์"""
        grid1 = ["abc", "lmp", "qrt"]
        self.assertEqual(Grid(grid1), "YES")
        
        grid2 = ["mpxz", "abcd", "wlmf"]
        self.assertEqual(Grid(grid2), "NO")

    def test_integeration_with_main(self):
        """ทดสอบการทำงานร่วมกับฟังก์ชัน main"""
        test_input = "2\n3\nabc\nlmp\nqrt\n3\nmpxz\nabcd\nwlmf"
        expected_output = "YES\nNO\n"
        
        # จำลองการรับ input และตรวจสอบ output
        with patch('sys.stdin', StringIO(test_input)), patch('sys.stdout', StringIO()) as fake_out:
            # จำลองการรัน main function
            t = int(input().strip())
            for t_itr in range(t):
                n = int(input().strip())
                grid = []
                for _ in range(n):
                    grid_item = input()
                    grid.append(grid_item)
                result = Grid(grid)
                print(result)
            
            self.assertEqual(fake_out.getvalue(), expected_output)
