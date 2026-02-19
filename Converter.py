from collections import defaultdict

class Converter:
    def __init__(self, facts) -> None:
        self.index = defaultdict(list)
        for from_unit, to_amt, to_unit in facts:
            self.index[from_unit].append((to_unit, to_amt))
            if to_amt != 0:
                self.index[to_unit].append((from_unit, 1 / to_amt))

    def answer(self, query) -> str:
        queue = []
        visited = set()

        from_amt, from_unit, target_unit = query
        queue.append((from_amt, from_unit))

        while queue:
            amt, unit = queue.pop()
            if unit == target_unit:
                return f"{from_amt} {from_unit} = {amt} {target_unit}"
            if unit in visited or unit not in self.index:
                continue
            visited.add(unit)
            for to_unit, to_amt in self.index[unit]:
                queue.append((to_amt * amt, to_unit))

        return "Not Found"


def main():
    facts = [
        ("m", 100, "cm"),
        ("cm", 10, "mm"),
        ("hr", 60, "min"),
        ("min", 60, "sec")
    ]
    converter = Converter(facts)
    print(converter.answer((0.04, "m", "cm")))
    print(converter.answer((60*60*4, "sec", "hr")))
    return

if __name__ == "__main__":
    main()