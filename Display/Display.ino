#include <LiquidCrystal_I2C.h>

const int button_right = 3;
const int button_left = 4;
int state_button_right = 0;
int state_button_left = 0;

int TRex_UP11 = 1;
int TRex_UP12 = 2;
int TRex_UP21 = 3;
int TRex_UP22 = 4;
int TRex_DOWN1 = 5;
int TRex_DOWN2 = 6;

int dirt_1 = 7;
int dirt_2 = 8;

int bird_1 = 9;
int bird_2 = 10;

int cactus_1 = 11;
int cactus_2 = 12;

LiquidCrystal_I2C lcd(0x27, 20, 04);

int gerarInt(int inicio, int fim)
{
    int intervalo = (++fim - inicio);
    int n = (rand() % intervalo) + inicio;
    return n;
}

byte T_Rex0[8] = {
  B00000,
  B00000,
  B00001,
  B00001,
  B00001,
  B00001,
  B00001,
  B00011
};

byte T_Rex1[8] = {
  B11100,
  B11110,
  B10110,
  B11111,
  B11000,
  B11111,
  B11100,
  B11000
};

byte T_Rex2[8] = {
  B00011,
  B00111,
  B01111,
  B11111,
  B11111,
  B01100,
  B01100,
  B01110
};

byte T_Rex3[8] = {
  B11100,
  B11111,
  B11101,
  B11100,
  B11000,
  B10000,
  B10000,
  B11000
};

byte T_Rex4[8] = {
  B00000,
  B00000,
  B00001,
  B00111,
  B01111,
  B11111,
  B11100,
  B01110
};

byte T_Rex5[8] = {
  B00000,
  B00000,
  B10000,
  B11110,
  B11101,
  B11111,
  B10000,
  B11000
};

byte dirt1[8] = {
  B11111,
  B10010,
  B11111,
  B10111,
  B11010,
  B11011,
  B10110,
  B01101
};

byte dirt2[8] = {
  B11111,
  B11101,
  B11011,
  B00110,
  B11011,
  B01111,
  B11011,
  B10101
};

byte bird1[8] = {
  B00000,
  B00000,
  B10000,
  B01000,
  B11111,
  B01110,
  B00100,
  B00000
};

byte bird2[8] = {
  B00000,
  B00100,
  B11110,
  B01111,
  B11111,
  B00000,
  B00000,
  B00000
};

byte cactus1[8] = {
  B00000,
  B00010,
  B00010,
  B10110,
  B10100,
  B11101,
  B00111,
  B00100
};

byte cactus2[8] = {
  B01100,
  B00101,
  B00101,
  B10101,
  B10111,
  B10100,
  B11100,
  B00100
};

void setup()
{
  pinMode(button_right, INPUT);
  pinMode(button_left, INPUT);
  
  //Define o LCD com 20 colunas e 4 linhas
  lcd.init();
  lcd.setBacklight(HIGH);

  lcd.createChar(TRex_UP11, T_Rex0);
  lcd.createChar(TRex_UP12, T_Rex1);
  lcd.createChar(TRex_UP21, T_Rex2);
  lcd.createChar(TRex_UP22, T_Rex3);

  lcd.createChar(TRex_DOWN1, T_Rex4);
  lcd.createChar(TRex_DOWN2, T_Rex5);

  lcd.createChar(dirt_1, dirt1);
  lcd.createChar(dirt_2, dirt2);

  lcd.createChar(bird_1, bird1);
  lcd.createChar(bird_2, bird2);

  lcd.createChar(cactus_1, cactus1);
  lcd.createChar(cactus_2, cactus2);
  
  lcd.setCursor(1,2);
  lcd.write(TRex_DOWN1);
  lcd.write(TRex_DOWN2);
  
  lcd.setCursor(0,3);
  for (int i = 0; i < 20; i++) {
    delay(200);
    if (gerarInt(0, 1) == 1) {
      lcd.write(dirt_1);
    } else {
      lcd.write(dirt_2);
    };
  };

}

void loop()
{
  
}
