from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

SOLUTION_PATH = Path(__file__).with_name('Number of Islands.py')
SPEC = spec_from_file_location('lc_200_solution', SOLUTION_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f'Unable to load solution from {SOLUTION_PATH}')

SOLUTION_MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(SOLUTION_MODULE)
Solution = SOLUTION_MODULE.Solution


TEST_CASES = (
    ('empty grid', [], 0),
    ('single water cell', [['0']], 0),
    ('single land cell', [['1']], 1),
    (
        'all water',
        [
            ['0', '0', '0'],
            ['0', '0', '0'],
        ],
        0,
    ),
    (
        'one solid island',
        [
            ['1', '1', '1'],
            ['1', '1', '1'],
        ],
        1,
    ),
    (
        'diagonal land cells are separate',
        [
            ['1', '0', '1'],
            ['0', '1', '0'],
            ['1', '0', '1'],
        ],
        5,
    ),
    (
        'single row',
        [['1', '0', '1', '1', '0', '1']],
        3,
    ),
    (
        'single column',
        [['1'], ['1'], ['0'], ['1']],
        2,
    ),
    (
        'outer ring and isolated center',
        [
            ['1', '1', '1', '1', '1'],
            ['1', '0', '0', '0', '1'],
            ['1', '0', '1', '0', '1'],
            ['1', '0', '0', '0', '1'],
            ['1', '1', '1', '1', '1'],
        ],
        2,
    ),
    (
        'five irregular islands',
        [
            ['1', '1', '0', '0', '1'],
            ['1', '0', '0', '1', '1'],
            ['0', '0', '1', '0', '0'],
            ['1', '1', '0', '0', '1'],
        ],
        5,
    ),
)


class NumberOfIslandsTest(unittest.TestCase):
    def assert_all_cases(self, method_name: str) -> None:
        implementation = method_name.removeprefix('numIslands_').upper()
        print(f'\n{implementation} test cases:', flush=True)

        for case_name, grid, expected in TEST_CASES:
            with self.subTest(method=method_name, case=case_name):
                solution = Solution()
                method = getattr(solution, method_name)
                try:
                    actual = method(deepcopy(grid))
                except Exception as error:
                    print(
                        f'[ERROR] {case_name}: '
                        f'{type(error).__name__}: {error}',
                        flush=True,
                    )
                    raise

                result = 'PASS' if actual == expected else 'FAIL'
                print(
                    f'[{result}] {case_name}: '
                    f'expected={expected}, actual={actual}',
                    flush=True,
                )
                self.assertEqual(expected, actual)

    def test_dfs(self) -> None:
        self.assert_all_cases('numIslands_dfs')

    def test_bfs(self) -> None:
        self.assert_all_cases('numIslands_bfs')


if __name__ == '__main__':
    unittest.main(verbosity=2)
