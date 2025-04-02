# MkDocs Variable Randomizer Plugin

Basically the idea is to use random variable names in code snippets.
This can for example be used to make code snippets that are [harder to fingerprint](https://github.com/t3l3machus/PowerShell-Obfuscation-Bible?tab=readme-ov-file#rename-objects), thus useful for offensive code like AMSI bypasses.

## Installation

```bash
pip install mkdocs_variable_randomizer_plugin
```

## Usage

Add the plogin to your `mkdocs.yml`:

```yaml
plugins:
- search
- variable_randomizer
```

Prefix all variables that you want to have random names with `rand_`.
So for example if your code says:
```powershell
$message = "abc"
Write-Host $message
```

Change it to:
```powershell
$rand_message = "abc"
Write-Host $rand_message
```

Now when you build the page with `mkdocs serve` and visit the website, the listing should have random variable names like this:
```powershell
$UEtWeCI = "abc"
Write-Host $UEtWeCI
```

The variable names will change every time you reload the web page in your browser.
