# Plant UML
* [VS Code UML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)
* [Class Diagram Syntax](https://plantuml.com/class-diagram)
* [Squence Diagram Syntax](https://plantuml.com/sequence-diagram)

* install extension
    - VS Code Extension > PlantUML 2.13.12 > install
    ```
    brew cask install java
    brew install graphviz
    ```
settings > [plantuml server](https://www.plantuml.com/plantuml)

## Class Diagram
```plantuml
@startuml
class Card
class BlackJackCard
Card <|-- BlackJackCard

Card : face:str
Card : suit:str
Card : __init__()
Card : __repr__()
Card : getValue():int

BlackJackCard : getValue():int

Deck "1" o-- "many" BlackJackCard
Deck : stackOfCards:list
Deck : __init__()
Deck : shuffle()

class Player
class Dealer
Player <|-- Dealer

Player "many" o-- "1" Game
Player : addCardToHand()
Player : increaseWin()
Player : cleanHand()
Player : getHandValue():int
Player : hit():bool
Player : name:str
Player : hand:list
Player : win:intß

Dealer : hit():bool
Dealer : shuffle()
Dealer : deal():Card

Dealer "1" o-- "many" Deck

Game "1" -- "1" Dealer
Game : play()

@enduml
```

## Flowchart
[Flowchart UML](https://plantuml.com/activity-diagram-legacy)
```plantuml
@startuml
(*) --> "calculate hand values"

if "player>21 and dealer<=21" then
    --> "dealer win"
else if "player<=21 and dealer>21"
    --> "player win"
    -->(*)
else if "player>21 and dealer>21"
    --> "both busted!"
    -->(*)
else if "player==dealer"
    --> "no one win"
    -->(*)
else if "dealer>player"
    --> "dealer win"
    -->(*)
else 
    --> "player win"
endif
@enduml
```