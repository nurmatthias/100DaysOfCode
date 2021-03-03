################### Scope ####################

# Global Scope
enemies = 1

def increase_enemies():
    # local scope
    enemies = 2
    print(f"enemies inside function: {enemies}")

    # no block scope
    if 2 > 1:
        new_enemie = 1
    
    print(f"enemie inside blocks (if/loop): {new_enemie}")

def increase_enemies_global():
    # change global variable
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

increase_enemies_global()
print(f"enemies outside function: {enemies}")


################### Global constants ####################

# BestPractice constants in upper case
PI = 3.14159