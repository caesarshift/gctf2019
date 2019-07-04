import sys
import time
# Implements a simple stack-based VM
class VM:

  def __init__(self, rom):
    self.rom = rom
    self.accumulator1 = 0
    self.accumulator2 = 0
    self.instruction_pointer = 1
    self.stack = []
    self.foo = ""

  def dump(self):
    print("st", self.stack)
    print("a1", self.accumulator1)
    print("a2", self.accumulator2)
    print("ip", self.instruction_pointer, self.rom[self.instruction_pointer])
    # print("fo", self.foo)

  def step(self):
    print("----------------------")
    cur_ins = self.rom[self.instruction_pointer]

    print("STEP: ", cur_ins)
    # self.dump()

    self.instruction_pointer += 1
    fn = VM.OPERATIONS.get(cur_ins, None)

    if cur_ins[0] == '🖋':
      return
    if fn is None:
      raise RuntimeError("Unknown instruction '{}' at {}".format(
          repr(cur_ins), self.instruction_pointer - 1))
    else:
      print("calling", fn)
      fn(self)

    # x = input(">")

  def add(self):
    print("add")
    foo = self.stack.pop()
    bar = self.stack.pop()
    print("ADD", foo, bar)
    self.stack.append(foo + bar)

  def sub(self):
    print("sub")
    a = self.stack.pop()
    b = self.stack.pop()
    print("SUB", a, b)
    self.stack.append(b - a)

  def if_zero(self):
    print("if_zero")
    if self.stack[-1] == 0:
      print("IF_ZERO: true")
      while self.rom[self.instruction_pointer] != '😐':
        print("IF_ZERO: not 😐")
        if self.rom[self.instruction_pointer] in ['🏀', '⛰']:
          print("IF_ZERO: 🏀 or ⛰")
          break
        self.step()
    else:
      print("IF_ZERO: false")
      self.find_first_endif()
      self.instruction_pointer += 1

  def if_not_zero(self):
    print("if_not_zero")
    if self.stack[-1] != 0:
      print("IF_NOT_ZERO: true")
      while self.rom[self.instruction_pointer] != '😐':
        if self.rom[self.instruction_pointer] in ['🏀', '⛰']:
          break
        self.step()
    else:
      self.find_first_endif()
      self.instruction_pointer += 1

  def find_first_endif(self):
    print("find_first_endif")
    while self.rom[self.instruction_pointer] != '😐':
      print("not end if")
      self.instruction_pointer += 1
    print("end if")

  def jump_to(self):
    print("jump_to")
    marker = self.rom[self.instruction_pointer]
    if marker[0] != '💰':
      print('Incorrect symbol : ' + marker[0])
      raise SystemExit()
    marker = '🖋' + marker[1:]
    self.instruction_pointer = self.rom.index(marker) + 1

  def jump_top(self):
    print("jump_top")
    self.instruction_pointer = self.stack.pop()

  def exit(self):
    print("exit")
    print('\nDone.')
    raise SystemExit()

  def print_top(self):
    print("print_top")
    x = chr(self.stack.pop())
    self.foo = self.foo + x
    print("x: ", x, "\n")
    self.dump()
    sys.stdout.flush()

  def push(self):
    print("push")
    if self.rom[self.instruction_pointer] == '🥇':
      print("push accumulator1", self.accumulator1)
      self.stack.append(self.accumulator1)
    elif self.rom[self.instruction_pointer] == '🥈':
      print("push accumulator2", self.accumulator2)
      self.stack.append(self.accumulator2)
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          self.rom[self.instruction_pointer], str(self.instruction_pointer)))
    self.instruction_pointer += 1

  def pop(self):
    print("pop")
    if self.rom[self.instruction_pointer] == '🥇':
      self.accumulator1 = self.stack.pop()
    elif self.rom[self.instruction_pointer] == '🥈':
      self.accumulator2 = self.stack.pop()
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          self.rom[self.instruction_pointer], str(self.instruction_pointer)))
    self.instruction_pointer += 1

  def pop_out(self):
    print("pop_out")
    self.stack.pop()

  def load(self):
    print("load")
    num = 0

    if self.rom[self.instruction_pointer] == '🥇':
      acc = 1
    elif self.rom[self.instruction_pointer] == '🥈':
      acc = 2
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          self.rom[self.instruction_pointer], str(self.instruction_pointer)))
    self.instruction_pointer += 1

    while self.rom[self.instruction_pointer] != '✋':
      num = num * 10 + (ord(self.rom[self.instruction_pointer][0]) - ord('0'))
      self.instruction_pointer += 1

    if acc == 1:
      self.accumulator1 = num
    else:
      self.accumulator2 = num

    self.instruction_pointer += 1

  def clone(self):
    print("clone")
    self.stack.append(self.stack[-1])

  def multiply(self):
    print("multiply")
    a = self.stack.pop()
    b = self.stack.pop()
    self.stack.append(b * a)

  def divide(self):
    print("divide")
    a = self.stack.pop()
    b = self.stack.pop()
    self.stack.append(b // a)

  def modulo(self):
    print("modulo")
    a = self.stack.pop()
    b = self.stack.pop()
    self.stack.append(b % a)

  def xor(self):
    print("xor")
    a = self.stack.pop()
    b = self.stack.pop()
    self.stack.append(b ^ a)

  OPERATIONS = {
      '🍡': add,
      '🤡': clone,
      '📐': divide,
      '😲': if_zero,
      '😄': if_not_zero,
      '🏀': jump_to,
      '🚛': load,
      '📬': modulo,
      '⭐': multiply,
      '🍿': pop,
      '📤': pop_out,
      '🎤': print_top,
      '📥': push,
      '🔪': sub,
      '🌓': xor,
      '⛰': jump_top,
      '⌛': exit
  }


if __name__ == '__main__':
  # if len(sys.argv) != 2:
  #   print('Missing program')
  #   raise SystemExit()

  with open("program", 'r') as f:
    print('Running ....')
    all_ins = ['']
    all_ins.extend(f.read().split())
    vm = VM(all_ins)

    # for i,a in enumerate(all_ins):
    #   fn = vm.OPERATIONS.get(a, None)
    #   if fn:
    #     print("\n"+str(i)+":"+str(fn), end='')
    #   else:
    #     print(a, end='')

    while 1:
      vm.step()
      # print(vm.stack, vm.instruction_pointer)
