public class EliminarDuplicados {
    
    public static int[] eliminarDuplicados(int[] array) {
        // Paso 1: Contar elementos únicos
        int count = 0;
        
        for (int i = 0; i < array.length; i++) {
            boolean esUnico = true;
            
            // Verificar si este elemento ya apareció antes
            for (int j = 0; j < i; j++) {
                if (array[i] == array[j]) {
                    esUnico = false;
                    break;
                }
            }
            
            if (esUnico) {
                count++;
            }
        }
        
        // Paso 2: Crear array del tamaño correcto
        int[] resultado = new int[count];
        int index = 0;
        
        // Paso 3: Llenar el array con elementos únicos
        for (int i = 0; i < array.length; i++) {
            boolean esUnico = true;
            
            for (int j = 0; j < i; j++) {
                if (array[i] == array[j]) {
                    esUnico = false;
                    break;
                }
            }
            
            if (esUnico) {
                resultado[index] = array[i];
                index++;
            }
        }
        
        return resultado;
    }

    public static void main(String[] args) {
        int[] conDuplicados = {1, 2, 2, 3, 4, 4, 5};
        int[] sinDuplicados = eliminarDuplicados(conDuplicados);
        
        for (int num : sinDuplicados) {
            System.out.print(num + " ");
        }
    }
}