---
name: backend-discipline
description: Binding server-side constraints. Load before writing a server route, domain type, API contract, or any outbound network call. Covers ports-and-adapters layering, the Dependency Rule at identifier level, aggregate transaction boundaries, contract-first APIs with problem-details errors, idempotency, timeouts and circuit breakers, and the security baseline.
---

# Backend Discipline (backend-discipline)

Postgryph의 서버 측 규율입니다. 데이터베이스 자체를 다루는 기준은 `supabase-data` 스킬에 있고, 이 문서는 그 데이터를 감싸는 서버 코드의 기준을 정합니다.

## 1. Ports and Adapters


- **Every external interaction is a port** — Declare the interface in the application or domain layer that owns the need, and put the technology in an adapter that implements it.
- **The Dependency Rule is checked at the identifier level** — No framework, ORM, HTTP or driver type name may appear anywhere under `domain/` or `application/`. That includes web framework types, ORM entities and clients, driver connections, and request or response objects. If the name of a library appears in the domain, the layering is already broken.
- **Interfaces live inward, implementations outward** — A repository or gateway interface is declared beside the domain type it returns; its implementation lives in infrastructure and is wired at composition root.

## 2. Domain Model


- **Ubiquitous language, literally** — Name types, methods and events with the exact words domain experts use. If the business says a policy lapses, the method is `lapse()`, never `setStatus(3)`.
- **Aggregates reference by identity** — A field is `customerId: CustomerId`, never `customer: Customer`. Traversing to another aggregate through an object reference is a defect.
- **One aggregate per transaction** — Modify exactly one aggregate instance per transaction. When a use case must change several, the others are updated through a domain event and eventual consistency, and that lag is stated explicitly.
- **Pattern names mean what the catalog says** — Use `Repository`, `Unit of Work`, `Data Mapper`, `Service Layer` only when the thing matches the catalog definition. A class named `Repository` that returns DTOs and takes SQL is misnamed.

## 3. Complexity Gates


- **Single model by default** — Introduce CQRS only inside one bounded context, and only with a measured read/write asymmetry in load, shape or consistency need. Event sourcing requires a written justification of the replay, versioning and snapshot strategy before the first event type is defined.
- **Gradual replacement over rewrite** — Replace a running system incrementally behind a facade. Do not propose a cut-over rewrite of a system that is currently serving traffic.
- **Record the decision** — Any choice that is expensive to reverse (storage engine, transport, boundary split, consistency model) gets an ADR: context, decision, status, consequences. One file per decision, never edited after acceptance except to change its status.

## 4. Configuration and Boot


- **Config comes from the environment** — Read every deploy-varying value from environment variables at process start and fail loudly at boot when one is missing. Never read a committed config file for credentials, hostnames or feature flags, and never default a secret.
- **Fail fast at boot, not at first request** — Validate the entire configuration surface before the process reports ready.

## 5. Contracts and Errors


- **Contract first** — The API schema is written and reviewed before the handler. Every change runs a breaking-change diff against the published contract; a breaking change requires a new version, never a silent edit.
- **Problem details for every failure** — Return 4xx and 5xx as `application/problem+json` with a stable `type` URI, a `title`, and a `detail` that never leaks internal identifiers, stack frames or SQL.
- **Idempotency for unsafe retries** — Any non-idempotent endpoint a client may retry accepts an idempotency key and stores the result keyed on it.

## 6. Cross-Boundary Effects

- **스키마와 마이그레이션은 `supabase-data` 스킬이 담당함** — 확장 후 축소, 되돌림 가능 여부, 잠금 없는 DDL은 그 문서를 따릅니다.
- **Outbox for cross-boundary effects** — A state change and the message announcing it are committed in the same transaction through an outbox, never as a database write followed by a separate publish.

## 7. Stability on Every Outbound Call


- **Explicit finite timeouts** — Every outbound network call sets an explicit connect timeout and an explicit read or total timeout. Never rely on the library default, which is usually infinite.
- **Bounded blast radius** — Wrap each remote dependency in a circuit breaker and give it its own bounded resource pool so one slow dependency cannot exhaust the process.
- **Fail fast** — Reject work at the edge when a required dependency is already known to be unavailable, instead of queueing it.

## 8. Security Baseline


- **No string-interpolated SQL** — Parameterize every query. A query built by concatenation is a defect regardless of the input's apparent source.
- **Authorize the resource, not the route** — Check that this principal may act on this specific object, not merely that they are authenticated.
- **No secrets in the repository** — Credentials, keys and tokens never appear in source, fixtures, logs or error payloads.
