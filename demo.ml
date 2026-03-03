# multilingual WASM browser demo
# Compiled by the CI into assets/wasm/multilingual.wasm
# Showcases WAT-supported constructs: functions, loops, classes (v0.5.1 OOP).

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

class Counter:
    def __init__(self, start):
        self.value = start

    def increment(self):
        self.value = self.value + 1
        return self.value

let c = Counter(10)

for i in range(8):
    print(fibonacci(i))

print(c.increment())
print(c.increment())
print(c.increment())
