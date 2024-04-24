"""
pip install simpy
py.test --pyargs simpy
"""

import simpy # An asynchronous event dispatcher

def clock(env, name, tick):
    while True:
        print(name, env.now)
        yield env.timeout(tick)
        
if __name__ == '__main__':
    env = simpy.Environment()
    env.process(clock(env, 'fast', 0.5))
    env.process(clock(env, 'slow', 2))
    env.run(until=4.01)
    
    