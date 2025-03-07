import { configureStore, createSlice, PayloadAction } from "@reduxjs/toolkit";
import { TypedUseSelectorHook, useDispatch, useSelector } from "react-redux";
import WebSocketService from './WebSocketService.tsx'

// Define the state type
interface GlobalState {
  webSocketService: WebSocketService;
  value: str | null;
}

// Initial state
const initialState: GlobalState = {
  webSocketService: new WebSocketService(),
  value: "initial value",
};

const globalSlice = createSlice({
  name: "global",
  initialState,
  reducers: {
    setValue: (state, action: PayloadAction<string | null>) => {
      state.value = action.payload;
    },
  },
});


// Export actions
export const { setValue } = globalSlice.actions;

// Create store
export const store = configureStore({
  reducer: {
    global: globalSlice.reducer,
  },
});

// Infer RootState and AppDispatch types from the store
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

// Custom hooks for TypeScript safety
export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
