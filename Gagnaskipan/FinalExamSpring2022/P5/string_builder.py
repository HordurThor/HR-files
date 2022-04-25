

class StringBuilder:
    def __init__(self):
        self.the_string = ""
        self.undos = []
        self.redos = []

    def insert_into_string(self, start_index, ins_str, undo = False):
        if start_index < 0 or start_index > len(self.the_string):
            return # DO NOTHING (also don't undo or redo this)
        self.the_string = self.the_string[0:start_index] + ins_str + self.the_string[start_index:len(self.the_string)]
        if not undo:
            self.undos.append(["remove", start_index, len(ins_str)])
        if undo:
            self.redos.append(["remove", start_index, len(ins_str)])


    def remove_from_string(self, start_index, length, undo = False):
        if start_index < 0 or length < 0 or (start_index + length) > len(self.the_string):
            return # DO NOTHING (also don't undo or redo this)
        removed_string_part = self.the_string[start_index:start_index + length]
        self.the_string = self.the_string[0:start_index] + self.the_string[start_index + length:len(self.the_string)]
        if not undo:
            self.undos.append(["insert", start_index, removed_string_part])
        if undo:
            self.redos.append(["insert", start_index, removed_string_part])



    ###
        # Implement the next two operations below, undo() and redo()
        # You may have to change other operations and add operations to make it work correctly
    ###

    def undo(self):
        if self.undos == []:
            return
        if self.undos[-1][0] == "insert":
            self.insert_into_string(self.undos[-1][1], self.undos[-1][2], True)
        else:
            self.remove_from_string(self.undos[-1][1], self.undos[-1][2], True)
        del self.undos[-1]

    def redo(self):
        if self.redos == []:
            return
        if self.redos[-1][0] == "insert":
            self.insert_into_string(self.redos[-1][1], self.redos[-1][2])
        else:
            self.remove_from_string(self.redos[-1][1], self.redos[-1][2])
        del self.redos[-1]

    def __str__(self):
        return self.the_string


if __name__ == "__main__":

    sb = StringBuilder()
    sb.insert_into_string(0, "string")
    print("string: " + str(sb))
    sb.insert_into_string(3, "something")
    print("string: " + str(sb))
    sb.remove_from_string(5, 7)
    print("string: " + str(sb))
    sb.undo()
    print("string: " + str(sb))
    sb.undo()
    print("string: " + str(sb))
    sb.insert_into_string(4, "ki")
    print("string: " + str(sb))
    sb.undo()
    print("string: " + str(sb))
    sb.undo()
    print("string: " + str(sb))
    sb.undo()
    print("string: " + str(sb))

    print()


    sb = StringBuilder()
    sb.insert_into_string(0, "string")
    print("string: " + str(sb))
    sb.insert_into_string(3, "something")
    print("string: " + str(sb))
    sb.remove_from_string(5, 7)
    print("string: " + str(sb))
    sb.undo()
    print("string: " + str(sb))
    sb.undo()
    print("string: " + str(sb))
    sb.redo()
    print("string: " + str(sb))
    sb.redo()
    print("string: " + str(sb))
    sb.undo()
    print("string: " + str(sb))
    sb.undo()
    print("string: " + str(sb))
    sb.insert_into_string(4, "ki")
    print("string: " + str(sb))
    sb.redo()
    print("string: " + str(sb))
    sb.undo()
    print("string: " + str(sb))
    sb.undo()
    print("string: " + str(sb))
    sb.undo()
    print("string: " + str(sb))
