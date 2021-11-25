import pytest
from main import summa, raznost, umnojeniye, deleniye

def test_summa_pozitiv():
  assert summa(2,4) == 6

def test_raznost_pozitiv():
  assert raznost(2,4) == -2

def test_umnojeniye_pozitiv():
  assert umnojeniye(2,4) == 8

def test_deleniye_pozitiv():
  assert deleniye(2,0) == 'На ноль делить нельзя!'

def test_summa_negativ():
  assert summa(2,4) != 7

def test_raznost_negativ():
  assert raznost(2,4) != 3

def test_umnojeniye_negativ():
  assert umnojeniye(2,4) != 7

def test_deleniye_negativ():
  assert deleniye(2,0) != 6