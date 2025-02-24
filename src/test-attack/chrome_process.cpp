#include <windows.h>
#include <iostream>

int main(int argc, char* argv[]) {
    // Ruta del ejecutable de Chrome
    const char* chromePath = R"(C:\Program Files\Google\Chrome\Application\chrome.exe)";
    const char* arguments = R"( https://www.carrefour.es/ --remote-debugging-port=9222 --user-data-dir="C:/chrome-debug" --disable-features=SameSiteByDefaultCookies )";

    STARTUPINFO si = { sizeof(STARTUPINFO) };
    PROCESS_INFORMATION pi;

    // Crear un objeto de trabajo (Job Object)
    HANDLE job = CreateJobObject(NULL, NULL);
    if (job == NULL) {
        std::cerr << "Error al crear Job Object: " << GetLastError() << std::endl;
        return 1;
    }

    // Configurar el Job Object para que termine todos los procesos si el padre muere
    JOBOBJECT_EXTENDED_LIMIT_INFORMATION jobInfo = {};
    jobInfo.BasicLimitInformation.LimitFlags = JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE;
    if (!SetInformationJobObject(job, JobObjectExtendedLimitInformation, &jobInfo, sizeof(jobInfo))) {
        std::cerr << "Error al configurar Job Object: " << GetLastError() << std::endl;
        CloseHandle(job);
        return 1;
    }

    // Crear el proceso hijo
    if (CreateProcess(
        chromePath,       // Ruta del ejecutable
        (LPSTR)arguments, // Argumentos
        NULL,             // Seguridad del proceso
        NULL,             // Seguridad del hilo
        FALSE,            // Heredar handles
        CREATE_SUSPENDED, // Crear en estado suspendido para asociarlo al Job
        NULL,             // Entorno
        NULL,             // Directorio de trabajo
        &si,              // Información de inicio
        &pi               // Información del proceso
    )) {
        // Asociar el proceso hijo al Job
        if (!AssignProcessToJobObject(job, pi.hProcess)) {
            std::cerr << "Error al asignar el proceso hijo al Job Object: " << GetLastError() << std::endl;
            TerminateProcess(pi.hProcess, 1);
            CloseHandle(pi.hProcess);
            CloseHandle(pi.hThread);
            CloseHandle(job);
            return 1;
        }

        // Reanudar el proceso hijo
        ResumeThread(pi.hThread);

        std::cout << "Proceso hijo iniciado correctamente con PID: " << pi.dwProcessId << std::endl;

		while (true) {
			Sleep(1000); // Dormir por intervalos de 1 segundo para evitar consumir recursos innecesarios
		}
        std::cout << "Padre finaliza. Hijo sera terminado automáticamente." << std::endl;

        // Cerrar handles
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
        CloseHandle(job);
    } else {
        std::cerr << "Error al iniciar el proceso hijo: " << GetLastError() << std::endl;
    }

    return 0;
}
