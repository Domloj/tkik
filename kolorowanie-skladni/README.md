# Kolorowanie składni języka

## Zakres
* przygotowanie własnego spisu tokenów do kolorowania
* opracowanie diagramu przejść do rozpoznawania tokenów
* implementacja skanera z kolorowanem składni wejściowego formatu
* informacje wstępne o projektach

## Zadania
* Przygotuj tabelę tokenów własnego formatu.
* Bazując na przygotowanym własnym formacie np. na uproszczonym języku programowania, napisz program kolorujący składnię.
* Zaimplementuj i wykorzystaj skaner rozpoznający tokeny wg przygotowanej tabeli tokenów. 
* Program powinien wczytywać z pliku kod w wybranym formacie i zwrócić do innego pliku pokolorowany kod. 
* Jako formatu wyjściowego można wykorzystać np. HTML. W pliku wyjściowym powinien być zachowany układ tekstu z pliku wejściowego.

# Dokumentacja Tokenów

## Operatory

| Symbol | Nazwa       | Kategoria   |
|--------|------------|------------|
| `+`    | Plus       | Operator   |
| `-`    | Minus      | Operator   |
| `*`    | Multiply   | Operator   |
| `/`    | Divide     | Operator   |
| `=`    | Assign     | Operator   |
| `%`    | Modulo     | Operator   |
| `<`    | Less       | Compare    |
| `>`    | More       | Compare    |
| `,`    | Comma      | Operator   |
| `;`    | Semicolon  | Operator   |
| `:`    | Colon      | Operator   |
| `!`    | Negation   | Operator   |

## Nawiasy

| Symbol | Nazwa      | Kategoria  |
|--------|-----------|-----------|
| `(`    | Param_L  | Brackets  |
| `)`    | Param_P  | Brackets  |
| `{`    | Curly_L  | Brackets  |
| `}`    | Curly_P  | Brackets  |
| `'`    | Single_quote  | Text  |
| `"`    | Double_quote  | Text  |


## Operatory logiczne i specjalne

| Symbol  | Nazwa               | Kategoria  |
|---------|--------------------|------------|
| `&&`    | Conjuction         | Logic      |
| `\|\|`  | Alternative        | Logic      |
| `:=`    | Colon Assign       | Operator   |
| `==`    | Comparison         | Compare    |
| `!=`    | Neg Comparison     | Compare    |
| `<=`    | Less Equal         | Compare    |
| `>=`    | More Equal         | Compare    |
| `++`    | Increase           | Operator   |
| `--`    | Decrease           | Operator   |
| `//`    | Comment Line       | Comment    |
| `/*`    | Comment Block Start | Comment    |
| `*/`    | Comment Block End   | Comment    |

## Słowa kluczowe

| Symbol   | Nazwa     | Kategoria |
|----------|----------|-----------|
| `if`     | If       | Keyword   |
| `else`   | Else     | Keyword   |
| `for`    | For      | Keyword   |
| `return` | Return   | Keyword   |
| `func`   | Func     | Keyword   |
| `var`    | Var      | Keyword   |

## Typy danych

| Symbol   | Nazwa  | Kategoria |
|----------|-------|-----------|
| `string` | Type  | Type      |
| `int`    | Type  | Type      |
| `text`   | Text  | Text      |

## Pozostałe

| Symbol   | Nazwa         | Kategoria |
|----------|--------------|-----------|
| `print`  | Print        | Keyword   |
| `number` | Number       | Number    |

## Kolory tokenów

| Token       | Znaczenie             | Kolor        |
|-------------|-----------------------|--------------|
| `if`        | Warunek               | Malinowy     |
| `else`      | Inaczej               | Niebieski    |
| `for`       | Pętla                 | Fioletowy    |
| `return`    | Zwracanie wartości    | Granatowy    |
| `func`      | Deklaracja funkcji    | Różowy       |
| `var`       | Deklaracja zmiennej   | Pomarańczowy |
| `string`    | Typ tekstowy          | Żółty        |
| `int`       | Typ całkowity         | Żółty        |
| `print`     | Drukowanie wyniku     | Niebieski    |
| `text `     | Dane tekstowe         | Niebieski    |
| `comment`   | Komentarze            | Zielony      |
| `+ - * / %` | Operatory matematyczne | Brązowy      |
| `&& \|\| !`   | Operatory logiczne    | Brązowy    |
| `== != < > <= >=` | Operatory porównania | Żółty  |
| `123, 3.14` | Liczby                | Seledynowy   |
| `//`        | Komentarz jednoliniowy | Zielony      |
| `/* ... */` | Komentarz wieloliniowy | Zielony      |
| `" ... "` | Dane tekstowe | Zielony      |
| `(` `)` `{` `}` `[ ]` | Nawiasy      | Czerowny |
| `, ;`       | Separatory            | Biały       |

## Struktura pliku i wykonanie

```
/project/src/skaner
  ├── main.go
  ├── functions/ #Zawiera funkcję process_expression() i scanner()
  │   ├── scanner.go
  ├── tokeny/ #Zawiera spis symboli, id_tokenów i ich kategorie
  │   ├── tokens.go
  ├── input.txt
  ├── output.html
  ├── go.mod
```

Aby uruchomić program:

```
python main.py -file input.txt
```