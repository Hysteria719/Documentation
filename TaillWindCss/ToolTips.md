###
    <div class="flex h-screen items-center justify-center">
        <div class="flex flex-col gap-12 items-center">
            <div class="
                relative 
                before:content-[attr(data-tip)]
                before:absolute
                before:px-4 before:py-2    
                before:left-1/2 before:-bottom-24
                before:w-max before:max-w-xs
                before:-translate-x-1/2
                before:-translate-y-full
                before:bg-gray-700 before:text-white
                before:rounded-md before:opacity-0
                before:transition-all

                after:absolute
                after:left-1/2 after:-bottom-4
                after:h-0 after:w-0
                after: -translate-x-1/2
                after:border-8    
                after:border-b-gray-700        
                after:border-l-transparent
                after:border-r-transparent
                after:border-t-transparent
                after:opacity-0
                after:transition-all

                hover:before:opacity-100 hover:after:opacity-100
                
                " 
                data-tip=" Message ToolTips">
                <button class="rounded bg-amber-400 text-white py-2 px-4 font-semibold shadow-md focus:outline-none">
                    Mon Bouton
                </button>
            </div>    
        </div>
    </div>
###