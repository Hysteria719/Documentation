interface Pagination {
    count: number;
    next: string;
    previous: string | null;
    limit: number;
}

interface PageSelected {
    offset: number;
    limit: number;
}
export type {Pagination, PageSelected}