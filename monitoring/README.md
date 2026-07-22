# Monitoring Stack

This folder runs Prometheus, Alertmanager, Grafana, and cAdvisor with Docker Compose.

## Start

```bash
cd /home/ec2-user/PROJECT-DOCKER/monitoring
docker compose up -d
```

## Check Containers

```bash
docker ps
```

Expected ports:

- Prometheus: `9090`
- Alertmanager: `9093`
- Grafana: `3000`
- cAdvisor: `8080`

## Test Prometheus Alerts

`alerts.yml` includes `AlertmanagerLiveTest`, which intentionally fires all the time.
This confirms Prometheus can load rules and send alerts to Alertmanager.

Check alerts in Prometheus:

```bash
curl -s http://localhost:9090/api/v1/alerts
```

Open in browser:

```text
http://EC2_PUBLIC_IP:9090/alerts
```

## Test Alertmanager Directly

Send one manual test alert directly to Alertmanager:

```bash
curl -X POST http://localhost:9093/api/v2/alerts \
  -H "Content-Type: application/json" \
  -d '[{"labels":{"alertname":"ManualAlertmanagerLiveTest","severity":"critical","source":"curl"},"annotations":{"summary":"Manual Alertmanager test from EC2"}}]'
```

Check Alertmanager received it:

```bash
curl -s http://localhost:9093/api/v2/alerts
```

Open in browser:

```text
http://EC2_PUBLIC_IP:9093/#/alerts
```

## Reload Prometheus After Rule Changes

The Compose file enables Prometheus lifecycle reload.

```bash
curl -X POST http://localhost:9090/-/reload
```

## Stop The Always-Firing Test Alert

After testing, edit `alerts.yml` and change:

```yaml
expr: vector(1)
```

to:

```yaml
expr: vector(0)
```

Then reload:

```bash
curl -X POST http://localhost:9090/-/reload
```
