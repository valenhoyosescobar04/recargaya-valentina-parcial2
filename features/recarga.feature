Feature: Módulo de recargas RecargaYa
  As a usuario de RecargaYa
  I want to recharge my phone correctly
  So that I receive the right bonus data

  Scenario: Recarga menor al minimo es rechazada
    Given un monto de recarga de 500 pesos
    When se procesa la recarga
    Then la recarga es rechazada

  Scenario: Recarga en rango minimo sin bonificacion
    Given un monto de recarga de 1000 pesos
    When se procesa la recarga
    Then la bonificacion es 0 por ciento

  Scenario: Recarga de 10000 recibe bonificacion del 10 por ciento
    Given un monto de recarga de 10000 pesos
    When se procesa la recarga
    Then la bonificacion es 10 por ciento

  Scenario: Recarga de 30000 recibe bonificacion del 25 por ciento
    Given un monto de recarga de 30000 pesos
    When se procesa la recarga
    Then la bonificacion es 25 por ciento

  Scenario: Usuario premium recibe 5 por ciento adicional
    Given un usuario premium con recarga de 10000 pesos
    When se procesa la recarga
    Then la bonificacion es 15 por ciento

  Scenario Outline: Tabla de bonificaciones por monto
    Given un monto de recarga de <monto> pesos
    When se procesa la recarga
    Then la bonificacion es <bonificacion> por ciento

    Examples:
      | monto | bonificacion |
      | 5000  | 0            |
      | 10000 | 10           |
      | 29999 | 10           |
      | 30000 | 25           |
      | 50000 | 25           |