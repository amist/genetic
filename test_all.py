import sys
from ge.core.genetic_executor import GeneticExecutor
from ge.problems.sphere import Sphere

def test_problem(problem, min_max, target_value):
    print(problem, end=' ')
    sys.stdout.flush()
    TIMES_TO_FAIL = 5
    
    ge_config = {
                 'problem': problem,
                 'environment_kwargs': {
                                        'min_max': min_max,
                                        'individual_kwargs': {
                                                              'size': 2
                                                             },
                                       },
                 
                }
                
    target_sign = 1
    if min_max == 'min':
        target_sign = -1
    
    # Randomized algorithm, so it needs to fail TIMES_TO_FAIL times to be considered failure
    for _ in range(TIMES_TO_FAIL):
        ge = GeneticExecutor(**ge_config)    
        solution = ge.get_solution()
        print(solution.get_fitness_value(), end=' ')
        sys.stdout.flush()
        try:
            assert target_sign * solution.get_fitness_value() >= target_sign * target_value
        except AssertionError:
            # Don't do anything. Will fail outside of the loop after TIMES_TO_FAIL times
            pass
        except Exception:
            break
        else:
            print('OK')
            return True
    print('FAIL')
    return False


def test_all():
    result = True
    result &= test_problem('Sphere', 'min', 1)
    result &= test_problem('Sphere', 'max', 24)
    
    if result:
        print('OK')
    else:
        print('FAIL')
        sys.exit(1)
    
    
if __name__ == '__main__':
    test_all()