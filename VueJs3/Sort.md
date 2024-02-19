###
    const sortByColumn = (column: string) => {    
        if (sorting.value.column === column) {
            if (sorting.value.order === 'asc') {
                sorting.value.order = 'desc';
            }
            else {
                sorting.value.order = 'asc';
            }
        }
        else {
            sorting.value.order='asc'
        }
        sorting.value.column = column;

        packages.value.sort((a: any, b: any) => {
            const aValue = a[column];
            const bValue = b[column];

            
            if (sorting.value.order === 'asc') {            
                return aValue.localeCompare ? aValue.localeCompare(bValue) : aValue - bValue;
            }
            else {
                return bValue.localeCompare ? bValue.localeCompare(aValue) : bValue - aValue;
            }
        })
        
    }
    const sortingIconClass = () => {
        return sorting.value.order === 'asc' ? 'bi bi-caret-up-fill' : 'bi bi-caret-down-fill';
    }

    <th class="colTri" scope="col" @click="sortByColumn('startCity')">Départ
                            <i v-if="sorting.column === 'startCity'" :class="sortingIconClass()"></i>
                            <i v-else class="bi bi-filter"></i>
    </th>
###