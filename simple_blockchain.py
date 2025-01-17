import hashlib
import time
import random

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, delay):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.delay = delay  # Добавляем задержку как атрибут

    def __str__(self):
        return f"Block {self.index} [{self.timestamp:.2f}] : {self.data} | Hash: {self.hash} | Delay: {self.delay:.2f} seconds"

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Создаёт первый блок в цепочке"""
        timestamp = time.time()  # Получаем текущий timestamp
        genesis_block = Block(0, "0", timestamp, "Genesis Block", self.calculate_hash(0, "0", "Genesis Block", timestamp), 0)
        self.chain.append(genesis_block)

    def calculate_hash(self, index, previous_hash, data, timestamp):
        """Вычисляет хеш блока"""
        value = str(index) + previous_hash + str(timestamp) + data
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def add_block(self, data):
        """Добавляет новый блок в цепочку с задержкой"""
        last_block = self.chain[-1]
        index = last_block.index + 1
        timestamp = time.time()  # Получаем текущий timestamp
        delay = random.uniform(2, 5)  # Задержка от 2 до 5 секунд
        time.sleep(delay)  # Ожидание перед созданием нового блока
        hash = self.calculate_hash(index, last_block.hash, data, timestamp)
        block = Block(index, last_block.hash, timestamp, data, hash, delay)
        self.chain.append(block)
        print(f"Block {index} [{timestamp:.2f}] : {data} | Hash: {hash} | Delay: {delay:.2f} seconds.")  # Форматируем вывод

    def print_chain(self):
        """Печатает всю цепочку блоков"""
        print("\nFull Blockchain:")
        for block in self.chain:
            print(block)

# Пример использования
if __name__ == "__main__":
    blockchain = Blockchain()
    
    # Добавляем 120 блоков с задержками
    for i in range(1, 121):
        blockchain.add_block(f"Data for block {i}")
    
    blockchain.print_chain()  # Печатаем всю цепочку в конце
