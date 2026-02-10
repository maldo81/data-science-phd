---
name: frontend-design
description: Build intentional, production-grade frontend interfaces with a distinct visual direction. Use when creating or redesigning pages, components, or interaction surfaces.
---

# Frontend Design

Use this skill for UI implementation tasks where visual quality and clarity matter.

## Intent

Produce interfaces that feel deliberate, not generic.

Pick and commit to a clear direction:
- editorial
- utilitarian
- expressive
- playful
- minimalist
- dense/professional

## Design Checklist

1. Choose a clear visual direction before coding.
2. Define typography intentionally; avoid default system stacks unless required by project constraints.
3. Use a coherent color system with CSS variables.
4. Add a non-flat background treatment (gradient, texture, or shape system) when appropriate.
5. Apply motion intentionally for hierarchy and state clarity.
6. Preserve accessibility: contrast, keyboard behavior, semantic structure.
7. Ensure responsive behavior on mobile and desktop.

## Do / Don’t

Do:
- make layout and type choices that match the product context
- use consistent spacing and visual rhythm
- keep interactions explainable and testable

Don’t:
- ship interchangeable boilerplate UI
- overuse decorative effects that reduce readability
- silently break established design-system constraints in an existing product

## Definition of Done

A UI task is done when:
- visual direction is explicit and coherent
- responsive behavior is verified
- accessibility basics are satisfied
- changes are consistent with project patterns (or deviations are documented)
- implementation is production-ready, not mockup-only
