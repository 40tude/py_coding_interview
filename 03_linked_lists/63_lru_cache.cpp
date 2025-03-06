#include <iostream>
#include <unordered_map>
#include <memory>

struct DoublyLinkedListNode {
    int key;
    int val;
    DoublyLinkedListNode* prev;
    DoublyLinkedListNode* next;
    DoublyLinkedListNode(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
};

class LRUCache {
public:
    explicit LRUCache(int capacity) : capacity(capacity) { // implicit conversion is forbidden
        head = std::make_unique<DoublyLinkedListNode>(-1, -1);
        tail = std::make_unique<DoublyLinkedListNode>(-1, -1);
        head->next = tail.get();
        tail->prev = head.get();
    }

    int get(int key) {
        if (hashmap.find(key) == hashmap.end()) return -1;
        DoublyLinkedListNode* node = hashmap[key];
        removeNode(node);
        addToTail(node);
        return node->val;
    }

    void put(int key, int value) {
        if (hashmap.find(key) != hashmap.end()) {    
            removeNode(hashmap[key]);
            delete hashmap[key];
            hashmap.erase(key);
        }

        if (hashmap.size() >= capacity) {
            DoublyLinkedListNode* lru = head->next;
            removeNode(lru);
            hashmap.erase(lru->key);
            delete lru;
        }

        DoublyLinkedListNode* newNode = new DoublyLinkedListNode(key, value);
        hashmap[key] = newNode;
        addToTail(newNode);
    }

    ~LRUCache() {
        for (auto& [key, node] : hashmap) {
            delete node;
        }
    }

    friend std::ostream& operator<<(std::ostream& os, const LRUCache& cache) {
        DoublyLinkedListNode* current = cache.head->next;
        std::cout << "LRUCache: ";
        while (current != cache.tail.get()) {
            std::cout << current->val << " ";
            current = current->next;
        }
        std::cout << "\n";
        return os;
    }

private:
    int capacity;
    std::unordered_map<int, DoublyLinkedListNode*> hashmap;
    std::unique_ptr<DoublyLinkedListNode> head;
    std::unique_ptr<DoublyLinkedListNode> tail;

    void addToTail(DoublyLinkedListNode* node) {
        node->prev = tail->prev;
        node->next = tail.get();
        tail->prev->next = node;
        tail->prev = node;
    }

    void removeNode(DoublyLinkedListNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
};

int main() {
    LRUCache cache(3);
    cache.put(1, 100);
    cache.put(2, 250);
    std::cout << cache.get(2) << "\n"; // 250
    cache.put(4, 300);
    cache.put(3, 200);
    std::cout << cache.get(4) << "\n"; // 300
    std::cout << cache.get(1) << "\n"; // 100
    std::cout << cache;
    return 0;
}
