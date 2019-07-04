import std.stdio;
import std.file;

// Implements a simple stack-based VM
class VM {
    string rom;
    integer accumulator1;
    integer accumulator2;
    integer instruction_pointer;
    int[] stack;

    // constructor
    this(string rom) {
        this.rom = rom;
        this.accumulator1 = 0;
        this.accumulator2 = 0;
        this.instruction_pointer = 1;
        this.stack = new int[0];
    }

    void dump() {
        writeln("----------------------\n");
        writeln("st", this.stack);
        writeln("a1", this.accumulator1);
        writeln("a2", this.accumulator2);
        writeln("ip", this.instruction_pointer);
        writeln("fo", this.foo);
    }

    void step(this){
        int cur_ins = this.rom[this.instruction_pointer];
        this.instruction_pointer.inc(1);

        fn = VM.OPERATIONS.get(cur_ins, None);

        if (cur_ins[0] == '🖋'): {
          return;
        }

        if (fn is None) {
          throw new Exception("Unknown instruction");  
           //'{}' at {}".format(repr(cur_ins), this.instruction_pointer - 1))
        }  else {
          fn(this)
        }

        writeln(this.stack)
    }

    int add():
        this.stack.append(this.stack.pop() + this.stack.pop())

}


//class VM:



  def add(this):
    

  def sub(this):
    a = this.stack.pop()
    b = this.stack.pop()
    this.stack.append(b - a)

  def if_zero(this):
    if this.stack[-1] == 0:
      while this.rom[this.instruction_pointer] != '😐':
        if this.rom[this.instruction_pointer] in ['🏀', '⛰']:
          break
        this.step()
    else:
      this.find_first_endif()
      this.instruction_pointer += 1

  def if_not_zero(this):
    if this.stack[-1] != 0:
      while this.rom[this.instruction_pointer] != '😐':
        if this.rom[this.instruction_pointer] in ['🏀', '⛰']:
          break
        this.step()
    else:
      this.find_first_endif()
      this.instruction_pointer += 1

  def find_first_endif(this):
    while this.rom[this.instruction_pointer] != '😐':
      this.instruction_pointer += 1

  def jump_to(this):
    marker = this.rom[this.instruction_pointer]
    if marker[0] != '💰':
      writeln('Incorrect symbol : ' + marker[0])
      raise SystemExit()
    marker = '🖋' + marker[1:]
    this.instruction_pointer = this.rom.index(marker) + 1

  def jump_top(this):
    this.instruction_pointer = this.stack.pop()

  def exit(this):
    writeln('\nDone.')
    raise SystemExit()

  def writeln_top(this):
    x = chr(this.stack.pop())
    this.foo = this.foo + x
    writeln(x, "\n")
    this.dump()
    sys.stdout.flush()

  def push(this):
    if this.rom[this.instruction_pointer] == '🥇':
      this.stack.append(this.accumulator1)
    elif this.rom[this.instruction_pointer] == '🥈':
      this.stack.append(this.accumulator2)
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          this.rom[this.instruction_pointer], str(this.instruction_pointer)))
    this.instruction_pointer += 1

  def pop(this):
    if this.rom[this.instruction_pointer] == '🥇':
      this.accumulator1 = this.stack.pop()
    elif this.rom[this.instruction_pointer] == '🥈':
      this.accumulator2 = this.stack.pop()
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          this.rom[this.instruction_pointer], str(this.instruction_pointer)))
    this.instruction_pointer += 1

  def pop_out(this):
    this.stack.pop()

  def load(this):
    num = 0

    if this.rom[this.instruction_pointer] == '🥇':
      acc = 1
    elif this.rom[this.instruction_pointer] == '🥈':
      acc = 2
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          this.rom[this.instruction_pointer], str(this.instruction_pointer)))
    this.instruction_pointer += 1

    while this.rom[this.instruction_pointer] != '✋':
      num = num * 10 + (ord(this.rom[this.instruction_pointer][0]) - ord('0'))
      this.instruction_pointer += 1

    if acc == 1:
      this.accumulator1 = num
    else:
      this.accumulator2 = num

    this.instruction_pointer += 1

  def clone(this):
    this.stack.append(this.stack[-1])

  def multiply(this):
    a = this.stack.pop()
    b = this.stack.pop()
    this.stack.append(b * a)

  def divide(this):
    a = this.stack.pop()
    b = this.stack.pop()
    this.stack.append(b // a)

  def modulo(this):
    a = this.stack.pop()
    b = this.stack.pop()
    this.stack.append(b % a)

  def xor(this):
    a = this.stack.pop()
    b = this.stack.pop()
    this.stack.append(b ^ a)

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
      '🎤': writeln_top,
      '📥': push,
      '🔪': sub,
      '🌓': xor,
      '⛰': jump_top,
      '⌛': exit
  }



void main() {


  if len(sys.argv) != 2:
    writeln('Missing program')
    raise SystemExit();

  
    int[] all_ins = new int[1];
    all_ins.

    File file = File("test.txt", "r"); 
    auto bytes = read("filename");
    file.close(); 

  with open(sys.argv[1], 'r') as f:
    writeln('Running ....')
    all_ins = ['']
    all_ins.extend(f.read().split())
    vm = VM(all_ins)

    # for i,a in enumerate(all_ins):
    #   fn = vm.OPERATIONS.get(a, None)
    #   if fn:
    #     writeln("\n"+str(i)+":"+str(fn), end='')
    #   else:
    #     writeln(a, end='')

    while 1:
      vm.step()
      # writeln(vm.stack, vm.instruction_pointer)


  VM vm = new VM;



}
