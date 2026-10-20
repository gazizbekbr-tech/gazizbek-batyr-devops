# gazizbek-batyr-devops

DevOps laboratory work: Linux → Git → GitHub → Docker → Jenkins.

| Element          | Value                     |
|------------------|---------------------------|
| Student          | Batyr Gazizbek        |
| Group            | IT2-2301                  |
| Student ID       | 38091             |
| Docker image     | gazizbek-batyr-devops                  |
| Docker container | gazizbek-batyr-container              |
| Jenkins job      | Gazizbek_Batyr_DevOps                    |

## Structure

```
app/        Python application + tests
scripts/    Bash scripts
config/     Configuration files
logs/       Logs (ignored by git)
backup/     Backups (ignored by git)
```

## Run

```bash
./scripts/Gazizbek_Batyr_system.sh
docker build -t gazizbek-batyr-devops .
docker run --name gazizbek-batyr-container gazizbek-batyr-devops
docker compose up
```
Video demo: Tue Oct 20 00:33:46 UTC 2026
