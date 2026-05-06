class  cuentabancaria (ABC):
    def __init__(self, nuemero_cuenta; str, titular: str, saldo: float = 0) :
        self._numero_cuenta = numero_cuenta
        self._titular = titular
        self.saldo = saldo
        self._historial: list[dict] = []
    
    @abstractmethod         
    def calcular_comision(self, monto: float) -> float:
        pass
    @abstractmethod 
    def get_tipo_cuenta(self) -> str:
        pass

    def depositar(self, monto: float) -> bool:
     if monto <= 0:
       self._saldo += monto
       self._registrar_transaccion("Depósito", monto)
       return True
     return False
    def retirar(self, monto: float) -> bool:
     comision = self.calcular_comision(monto)
    total_retiro = monto + comision

    if total_retiro <= self._saldo:
        self._saldo -= total_retiro
        self._registrar_transaccion("Retiro",  -monto, f"comision; ${comision:,.0f}")
        return True
     return False
                                               
    def _registrar_transaccion(self, tipo: str, monto: float, detalle: str = ""):
        """Método protegido para registrar transacciones."""
        self._historial.append(
            {"fecha": datetime.now(), "tipo": tipo, "monto": monto, "detalle": detalle} )                                              
# Getters y Setters (Encapsulamiento)
    @property
    def saldo(self) -> float:
        return self._saldo
    @property
    def numero_cuenta(self) -> str:
        return self._numero_cuenta